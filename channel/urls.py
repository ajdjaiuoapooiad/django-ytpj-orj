
from django.contrib import admin
from django.urls import include, path

from channel import views

urlpatterns = [
    path("<channel_name>/",views.channel_profile,name='channel-profile'),
    path("<channel_name>/video/",views.channel_videos,name='channel-videos'),
    path("<channel_name>/about/",views.channel_about,name='channel-about'),
    path("<channel_name>/community/",views.channel_community,name='channel-community'),
    path("<channel_name>/community/<int:community_id>/",views.channel_community_detail,name='channel-community-detail'),
    
    # Create post
    path("channel/create-community-post/<channel_id>/",views.create_community_post,name='create-post'),
    path("channel/<int:community_id>/create-comment/",views.create_comment,name='create-comment'),

    
    # video-upload
    path('channel/create/video/',views.video_upload,name='video-upload'),
    path('channel/edit-video/<channel_id>/<video_id>/',views.video_edit,name='video-edit'),
    path('channel/delete-video/<video_id>/',views.video_delete,name='video-delete'),
    
]
