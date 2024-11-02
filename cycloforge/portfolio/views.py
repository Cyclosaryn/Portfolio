# portfolio/views.py
from django.shortcuts import render
from .models import Biography

def home(request):
    biography = Biography.objects.filter(name='Homepage').latest('created_at')
    context = {
        'biography': biography
    }
    return render(request, 'home.html', context)

def projects(request):
    return render(request, 'projects.html')