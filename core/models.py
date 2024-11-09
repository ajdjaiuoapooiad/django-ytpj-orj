
from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings

User=settings.AUTH_USER_MODEL





VISIBILITY=(
    ('private','Private'),
    ('public','Public'),
    ('members_only','Members_only'),
    
    
)



def user_derectory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)


class Video(models.Model):
    video=models.FileField(upload_to=user_derectory_path)
    image=models.ImageField(upload_to=user_derectory_path,null=True,blank=True)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=4000,null=True,blank=True)
    tags=TaggableManager(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    visibility=models.CharField(choices=VISIBILITY,max_length=100,default='public')
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    views=models.PositiveIntegerField(default=0)
    likes=models.ManyToManyField(User,blank=True,related_name='likes')
    featured=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
    
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="comments")
    comment=models.TextField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.comment[:30]
    
    
    