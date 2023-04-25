from django.urls import path

from django.contrib import admin
from . import models, views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]