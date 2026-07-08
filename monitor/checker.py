import requests
import time
import logging
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Website, MonitorLog, Notification
from .email_templates import (
    website_down_email,
    website_up_email,
    website_slow_email,
)

logger = logging.getLogger(__name__)

HIGH_RESPONSE_THRESHOLD = 1000

User = get_user_model()


def get_notification_recipients():
    return ["dikshawayal@gmail.com"]


def send_website_email(subject, html_message):
    try:
        recipients = get_notification_recipients()
        if not recipients:
            logger.warning("No email recipients configured. Email not sent.")
            return

        email = EmailMultiAlternatives(
            subject=subject,
            body="This email requires HTML support. Please view this email in a modern email client.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=recipients,
        )
        email.attach_alternative(html_message, "text/html")
        email.send()

        logger.info(
            "Email delivered successfully via %s | Subject: %s | Recipients: %s",
            settings.EMAIL_HOST,
            subject,
            recipients,
        )

    except Exception as e:
        logger.error(
            "Email delivery failed via %s | Subject: %s | Error: %s",
            settings.EMAIL_HOST,
            subject,
            e,
        )


def check_website(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5, allow_redirects=True)
        response_time = round((time.time() - start_time) * 1000, 2)
        if 200 <= response.status_code < 400:
            status = "UP"
        else:
            status = "DOWN"
        return {
            'status': status,
            'status_code': response.status_code,
            'response_time': response_time,
        }
    except requests.exceptions.RequestException:
        return {
            'status': 'DOWN',
            'status_code': 0,
            'response_time': None,
        }


def create_notification(website, message, ntype):
    Notification.objects.create(
        website=website,
        message=message,
        type=ntype,
    )


def notify_check_result(website, result, prev_status):
    name = website.name
    rtime = result['response_time']
    status = result['status']

    if status == 'UP':
        if prev_status == 'DOWN':
            msg = f"[OK] {name} is back UP."
            create_notification(website, msg, Notification.SUCCESS)
            logger.info("Status change DOWN->UP for %s", name)

        elif rtime and rtime > HIGH_RESPONSE_THRESHOLD:
            msg = f"[WARN] {name} response time is high ({rtime} ms)."
            create_notification(website, msg, Notification.WARNING)
            logger.warning("High response time for %s: %sms", name, rtime)

        else:
            msg = f"[INFO] {name} checked successfully. Status: UP. Response Time: {rtime} ms."
            create_notification(website, msg, Notification.INFO)

    else:
        if prev_status == 'UP':
            msg = f"[DOWN] {name} is DOWN!"
            create_notification(website, msg, Notification.ERROR)
            html = website_down_email(website, result)
            send_website_email(
                subject=f"[ALERT] Critical Website Down Alert - {name}",
                html_message=html,
            )
            logger.warning("Status change UP->DOWN for %s", name)

        else:
            msg = f"[DOWN] {name} is still DOWN."
            create_notification(website, msg, Notification.WARNING)
            logger.warning("Still DOWN for %s", name)

    website.status = result['status']
    website.response_time = result['response_time']
    website.last_checked = timezone.now()
    website.save()

    MonitorLog.objects.create(
        website=website,
        status=result['status'],
        status_code=result['status_code'],
        response_time=result['response_time'],
    )


def check_all_websites():
    websites = Website.objects.all()
    stats = {
        'total': 0,
        'up': 0,
        'down': 0,
        'errors': 0,
    }

    logger.info("Starting check of all websites (%d total)", websites.count())

    for website in websites:
        stats['total'] += 1
        try:
            result = check_website(website.url)
            prev_status = website.status
            notify_check_result(website, result, prev_status)

            if result['status'] == 'UP':
                stats['up'] += 1
            else:
                stats['down'] += 1

            logger.info(
                "Checked %s (%s) - Status: %s, Response: %sms",
                website.name,
                website.url,
                result['status'],
                result['response_time'],
            )
        except Exception as e:
            stats['errors'] += 1
            msg = f"🔴 {website.name} check failed: {str(e)}"
            create_notification(website, msg, Notification.ERROR)
            logger.exception(
                "Unexpected error checking %s (%s): %s",
                website.name,
                website.url,
                str(e),
            )

    logger.info(
        "Check complete - Total: %d, UP: %d, DOWN: %d, Errors: %d",
        stats['total'],
        stats['up'],
        stats['down'],
        stats['errors'],
    )
    return stats
