# portfolio/management/commands/copy_db.py
from django.core.management.base import BaseCommand
from django.core import serializers
from portfolio.models import Biography, Project

class Command(BaseCommand):
    help = 'Copy all model entries to a JSON file'

    def handle(self, *args, **kwargs):
        with open('db_backup.json', 'w') as f:
            data = serializers.serialize('json', Biography.objects.all())
            f.write(data)
            data = serializers.serialize('json', Project.objects.all())
            f.write(data)
        self.stdout.write(self.style.SUCCESS('Successfully copied database entries to db_backup.json'))