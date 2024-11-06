
from django import forms

from channel.models import Channel, Community, CommunityComment
from core.models import Video




class VideoCreateForm(forms.ModelForm):
    

    class Meta:
        model=Video
        fields=[
            'video',
            'image',
            'title',
            'description',
            'tags',
            'visibility',
            'featured',
        ]
        


class CommunityCreateForm(forms.ModelForm):
    
    class Meta:
        model=Community
        fields=[
            'content',
            'image',
        ]

class ChannelEditForm(forms.ModelForm):
    
    class Meta:
        model=Channel
        fields=[
            'channel_art',
            'image',
            'full_name',
            'channel_name',
            'description',
            'keyword',
            'business_email',
            'make_business_email_public',
            'business_location',
            'make_business_location_public',
            
        ]


