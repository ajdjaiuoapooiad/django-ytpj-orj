
from django.contrib import admin
from django.urls import include, path

from channel import views

urlpatterns = [
    path("<channel_name>/",views.channel_profile,name='channel-profile'),
    
    
    path('channel/create/video/',views.video_upload,name='upload-video'),
]
