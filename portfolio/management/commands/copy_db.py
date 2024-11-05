# portfolio/management/commands/copy_db.py
from django.core.management.base import BaseCommand
from django.core import serializers
from portfolio.models import Biography, Project

class Command(BaseCommand):
    help = 'Copy all model entries to JSON files'

    def handle(self, *args, **kwargs):
        with open('biography_backup.json', 'w') as bio_file:
            data = serializers.serialize('json', Biography.objects.all())
            bio_file.write(data)
        
        with open('project_backup.json', 'w') as project_file:
            data = serializers.serialize('json', Project.objects.all())
            project_file.write(data)
        
        self.stdout.write(self.style.SUCCESS('Successfully copied database entries to JSON files'))