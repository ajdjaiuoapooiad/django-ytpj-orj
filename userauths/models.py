from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.db.models import Model

from core.models import Video



class User(AbstractUser):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True,null=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    
    def __str__(self):
        return self.username
    
    
    
class Profile(Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    save_video=models.ManyToManyField(Video,related_name='save_video',blank=True)
    
    def __str__(self):
        return self.user.username
    

def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
    
    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)