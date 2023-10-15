from django.core.management.base import BaseCommand
from NeoCoffee.models import Category, initialize_data

class Command(BaseCommand):
    help = 'Initialize data from JSON'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write(self.style.SUCCESS('Clearing existing data...'))
        Category.objects.all().delete()

        # Load new data
        self.stdout.write(self.style.SUCCESS('Loading data from JSON...'))
        initialize_data()

        self.stdout.write(self.style.SUCCESS('Data initialized successfully!'))
