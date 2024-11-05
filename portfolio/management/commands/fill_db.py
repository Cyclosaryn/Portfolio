# portfolio/management/commands/fill_db.py
from django.core.management.base import BaseCommand
from django.core import serializers
from portfolio.models import Biography, Project

class Command(BaseCommand):
    help = 'Fill the database with entries from JSON files'

    def handle(self, *args, **kwargs):
        with open('biography_backup.json', 'r') as bio_file:
            data = bio_file.read()
            for obj in serializers.deserialize('json', data):
                obj.save()
        
        with open('project_backup.json', 'r') as project_file:
            data = project_file.read()
            for obj in serializers.deserialize('json', data):
                obj.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully filled database with entries from JSON files'))