
from django.contrib import admin
from django.urls import include, path

from core import views

urlpatterns = [
    path('',views.index,name='index'),
    path('video/<int:pk>/',views.detail,name='video-detail'),
]
