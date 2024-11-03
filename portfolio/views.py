# portfolio/views.py
from django.shortcuts import render
from .models import Biography
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
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')