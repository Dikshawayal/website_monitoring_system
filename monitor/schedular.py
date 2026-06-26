from apscheduler.schedulers.background import BackgroundScheduler
from .models import Website, MonitorLog
from .checker import check_website
from django.utils import timezone


def monitor_all_websites():

    websites = Website.objects.all()

    for website in websites:

        result = check_website(website.url)

        website.status = result['status']
        website.response_time = result['response_time']
        website.last_checked = timezone.now()
        website.save()

        MonitorLog.objects.create(
            website=website,
            status=result['status'],
            status_code=result['status_code'],
            response_time=result['response_time']
        )


def start():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        monitor_all_websites,
        'interval',
        minutes=5
    )

    scheduler.start()