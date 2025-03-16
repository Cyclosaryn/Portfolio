from django.shortcuts import render
from portfolio import models


def hermeshome(request):
    contacts = models.Contact.objects.all()
    combined_context = {
        'contacts': contacts
    }
    return render(request, 'hermeshome.html', combined_context)