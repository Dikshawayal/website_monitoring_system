from django.core.management.base import BaseCommand
from monitor.models import Website
import requests


class Command(BaseCommand):
    help = "Check website status"

    def handle(self, *args, **kwargs):
        websites = Website.objects.all()

        for website in websites:
            try:
                response = requests.get(
                    website.url,
                    timeout=10
                )

                if response.status_code == 200:
                    website.status = "UP"
                else:
                    website.status = "DOWN"

            except:
                website.status = "DOWN"

            website.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Website checks completed"
            )
        )