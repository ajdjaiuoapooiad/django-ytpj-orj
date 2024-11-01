from django.db import models
from taggit.managers import TaggableManager
from core.models import user_derectory_path
from ytpj import settings
from django.db.models.signals import post_save


User=settings.AUTH_USER_MODEL





STATUS = (
    ('Active','Active'),
    ('Disabled','Disabled'),#垢ban
)



class Channel(models.Model):
    channel_art=models.ImageField(upload_to=user_derectory_path,default='images/channel-art.jpg')
    image=models.ImageField(upload_to=user_derectory_path,default='images/user-image.png')
    full_name=models.CharField(max_length=100)
    channel_name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    keyword=TaggableManager()
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS,max_length=100,default='Active')
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,related_name="channel")
    subscibers=models.ManyToManyField(User,related_name="user_subs",blank=True)
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
    
    def save(self, *args, **kwargs):
        if self.channel_name == "":
            self.channel_name = self.user.username
        super().save(*args, **kwargs)


def create_user_channel(sender, instance, created, **kwargs):
    if created:
        Channel.objects.create(user=instance)

def save_user_channel(sender, instance, **kwargs):
    instance.channel.save()

post_save.connect(create_user_channel, sender=User)
post_save.connect(save_user_channel, sender=User)
    

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.channel.user.id, filename)
    
    

class Community(models.Model):
    channel=models.ForeignKey(Channel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=user_derectory_path,null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS,default='Active',max_length=100)
    likes=models.ManyToManyField(User,blank=True)
    
    def __str__(self):
        return self.channel.channel_name
    
    class Meta:
        verbose_name='Community'
        verbose_name_plural='Community Posts'
    
    
    
    
class CommunityComment(models.Model):
    community=models.ForeignKey(Community,on_delete=models.CASCADE,related_name="comments")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.community.channel.channel_name
    
    
    class Meta:
        verbose_name='Community Comments'
        verbose_name_plural='Community Comments'
    
    
    
    
    