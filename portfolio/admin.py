from django.contrib import admin
from .models import Biography, Project, Contact

# Register your models here.
admin.site.register(Biography)
admin.site.register(Project)
admin.site.register(Contact)