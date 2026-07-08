import logging
from django.core.management.base import BaseCommand
from monitor.checker import check_all_websites

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Check all monitored websites and update their status"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Starting website monitoring check..."))

        try:
            stats = check_all_websites()

            self.stdout.write(self.style.SUCCESS(
                f"Check complete — Total: {stats['total']}, "
                f"UP: {stats['up']}, "
                f"DOWN: {stats['down']}"
            ))

            if stats['errors']:
                self.stdout.write(self.style.WARNING(
                    f"Errors encountered: {stats['errors']}"
                ))

            if stats['down']:
                self.stdout.write(self.style.WARNING(
                    f"{stats['down']} website(s) are DOWN"
                ))

        except Exception as e:
            logger.exception("Monitoring check failed: %s", str(e))
            self.stdout.write(self.style.ERROR(
                f"Monitoring check failed: {e}"
            ))
