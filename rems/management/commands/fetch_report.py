from django.core.management.base import BaseCommand

from rems.tasks import fetch_report


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(fetch_report())
