import logging
from .models import SchedulerStatus
from datetime import timedelta
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from .checker import check_all_websites

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()
job = None

def monitor_all_websites():
    """
    Function executed every 5 hours.
    """

    global job

    logger.info("========================================")
    logger.info("Scheduled Website Check Started")
    logger.info("========================================")

    try:
        # Check all websites
        check_all_websites()

        # Update scheduler status
        status, created = SchedulerStatus.objects.get_or_create(id=1)

        now = timezone.localtime()

        status.status = "Running"
        status.last_run = now
        current_job = scheduler.get_job("check_all_websites")
        if current_job:
            status.next_run = timezone.localtime(current_job.next_run_time)
        else:
            status.next_run = now + timedelta(hours=5)
        status.interval = "Every 5 Hours"
        status.save()

    except Exception as e:
        logger.exception("Scheduler Error: %s", e)

    logger.info("========================================")
    logger.info("Scheduled Website Check Finished")
    logger.info("========================================")
def start():
    """
    Starts APScheduler only once.
    """

    global job
    global scheduler_status

    if scheduler.running:
        logger.info("Scheduler already running.")
        return

    job = scheduler.add_job(
        monitor_all_websites,
        trigger="interval",
        hours=5,
        id="check_all_websites",
        name="Check all websites every 5 hours",
        replace_existing=True,
        next_run_time=timezone.now()
    )

    scheduler.start()
    status, created = SchedulerStatus.objects.get_or_create(id=1)
    status.status = "Running"
    status.next_run = timezone.localtime(job.next_run_time)
    status.interval = "Every 5 Hours"
    status.save()

    scheduler_status = "Running"

    logger.info("========================================")
    logger.info("APScheduler Started Successfully")
    logger.info("Job Name : %s", job.name)
    logger.info("Next Run : %s", timezone.localtime(job.next_run_time))
    logger.info("========================================")
def get_scheduler_info():
    """
    Returns current scheduler information.
    """
    status, created = SchedulerStatus.objects.get_or_create(id=1)

    return {
        "status": status.status,
        "last_run": status.last_run,
        "next_run": status.next_run,
        "interval": status.interval,
    }