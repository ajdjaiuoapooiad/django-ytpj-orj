
from django.contrib import admin
from django.urls import include, path

from channel import views

urlpatterns = [
    path("<channel_name>/",views.channel_profile,name='channel-profile'),
    
    # video-upload
    path('channel/create/video/',views.video_upload,name='upload-video'),
    path('channel/edit-video/<channel_id>/<video_id>/',views.video_edit,name='edit-video'),
]
