import os
import logging
from django.apps import AppConfig

logger = logging.getLogger(__name__)


class MonitorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "monitor"

    def ready(self):

        # Prevent scheduler from starting twice
        if os.environ.get("RUN_MAIN") != "true":
            return

        try:
            from .schedular import start
            start()
            logger.info("APScheduler started successfully.")
        except Exception as e:
            logger.error("Scheduler failed to start: %s", e)