
from django.contrib import admin
from django.urls import include, path

from core import views

urlpatterns = [
    path('',views.index,name='index'),
    path('video/<int:pk>/',views.detail,name='video-detail'),
    
    # Ajax
    path('ajax-save-comment/',views.ajax_save_comment,name='save-comment'),
    path('ajax-delete-comment/',views.ajax_delete_comment,name='delete-comment'),
]
