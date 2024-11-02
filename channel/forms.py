
from django import forms

from channel.models import Community
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