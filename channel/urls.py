
from django.contrib import admin
from django.urls import include, path

from channel import views

urlpatterns = [
    path("<channel_name>/",views.channel_profile,name='channel-profile'),
    path("<channel_name>/video/",views.channel_videos,name='channel-videos'),
    path("<channel_name>/about/",views.channel_about,name='channel-about'),
    path("<channel_name>/community/",views.channel_community,name='channel-community'),
    path("<channel_name>/community/<int:community_id>/",views.channel_community_detail,name='channel-community-detail'),
    
    
    # video-upload
    path('channel/create/video/',views.video_upload,name='upload-video'),
    path('channel/edit-video/<channel_id>/<video_id>/',views.video_edit,name='edit-video'),
]
