
from django.contrib import admin
from django.urls import include, path

from core import views

urlpatterns = [
    path('',views.index,name='index'),
    path('video/<int:pk>/',views.detail,name='video-detail'),
    
    # Ajax
    path('ajax-save-comment/',views.ajax_save_comment,name='save-comment'),
    path('ajax-delete-comment/',views.ajax_delete_comment,name='delete-comment'),
    
    # Subscribe
    path('add-sub/<int:id>/',views.add_new_sub,name='add_sub'),
    path('load-sub/<int:id>/',views.load_sub,name='load_sub'),
    
    # Likes
    path('add-like/<int:id>/',views.add_new_like,name='add_like'),
    path('load-like/<int:id>/',views.load_like,name='load_like'),
    
    # Save-video
    path('add-save/<video_id>/',views.add_new_save,name='add_save'),
    
    # Search 
    path('video/search/',views.searchView,name='search'),
    
    # Tag
    path('video/tags/<slug:tag_slug>/',views.tagView,name='video-tag'),
    
]
