from django.contrib import admin
from django.urls import path, re_path, include
from hermes import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('home/', views.hermeshome),
]