# portfolio/management/commands/fill_db.py
from django.core.management.base import BaseCommand
from django.core import serializers
from portfolio.models import Biography, Project

class Command(BaseCommand):
    help = 'Fill the database with entries from a JSON file'

    def handle(self, *args, **kwargs):
        with open('db_backup.json', 'r') as f:
            data = f.read()
            for obj in serializers.deserialize('json', data):
                obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully filled database with entries from db_backup.json'))