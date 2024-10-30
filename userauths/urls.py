
from django.contrib import admin
from django.urls import  path

from userauths import views

urlpatterns = [
    path('sign-in/',views.loginView,name='sign-in'),
    path('sign-up/',views.registerView,name='sign-up'),
    path('sign-out/',views.logoutView,name='sign-out'),
    
]
