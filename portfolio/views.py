# portfolio/views.py
from django.shortcuts import render
from .models import Biography, Project
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", status=200)

def home(request):
    try:
        biography = Biography.objects.filter(name='Homepage').latest('created_at')
    except Biography.DoesNotExist:
        biography = None
    context = {
        'biography': biography
    }
    return render(request, 'home.html', context)

def projects(request):
    project = Project.objects.all().order_by('-created_at')
    
    context = {
        'projects': project
    }
    return render(request, 'projects.html', context)

def project_detail(request, id):
    project = Project.objects.get(id=id)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def contact(request):
    return render(request, 'contact.html')