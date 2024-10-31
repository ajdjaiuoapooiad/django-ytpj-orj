


from dataclasses import fields
from django import forms

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