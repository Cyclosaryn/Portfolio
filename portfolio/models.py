from django.db import models
import uuid
from tinymce.models import HTMLField

class Biography(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = HTMLField()
    profilepicture = models.ImageField(upload_to='profilepictures/', blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = HTMLField()
    projectpicture = models.ImageField(upload_to='projectpictures/', blank=True, null=True)

    def __str__(self):
        return self.name