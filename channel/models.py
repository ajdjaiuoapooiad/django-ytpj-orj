from django.db import models
from taggit.managers import TaggableManager
from core.models import user_derectory_path
from ytpj import settings

User=settings.AUTH_USER_MODEL


def user_derectory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)




STATUS = (
    ('Active','Active'),
    ('Disabled','Disabled'),
)



class Channel(models.Model):
    channel_art=models.ImageField(upload_to=user_derectory_path,default='images/channel-art.jpg')
    image=models.ImageField(upload_to=user_derectory_path,default='images/user-image.png')
    full_name=models.CharField(max_length=100)
    channel_name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    keyword=TaggableManager
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS,max_length=100,default='Active')
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="channel")
    subscibers=models.ManyToManyField(User,related_name="user_subs")
    verified=models.BooleanField(default=False)
    
    total_view=models.PositiveIntegerField(default=0)
    business_email=models.EmailField(null=True,blank=True)
    make_business_email_public=models.BooleanField(default=False)
    business_location=models.CharField(null=True,blank=True,max_length=100)
    make_business_location_public=models.BooleanField(default=False)
    
    
    website=models.URLField(default='https://www.udemy.com/home')
    instagram=models.URLField(default='https://www.udemy.com/home')
    facebook=models.URLField(default='https://www.udemy.com/home')
    twitter=models.URLField(default='https://www.udemy.com/home')
    
    def __str__(self):
        return self.channel_name
    