
from django.contrib import admin
from django.urls import include, path

from useradmin import views

urlpatterns = [
    path("",views.studio,name='studio'),
    
]
