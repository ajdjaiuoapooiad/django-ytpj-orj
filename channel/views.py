from django.shortcuts import get_object_or_404, redirect, render

from channel.forms import VideoCreateForm
from channel.models import Channel
from core.models import  Video
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def channel_profile(request,channel_name):
    channel = get_object_or_404(Channel,id=channel_name)
    
    
    context={
        'channel': channel,
    }
    return render(request,'channel/channel.html',context)



def video_upload(request):
    user=request.user
    
    if request.method=='POST':
        form=VideoCreateForm(request.POST,request.FILES)
        
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=user
            new_form.save()
            form.save_m2m()
            messages.success(request,f'Video uploaded successfully')
            return redirect('index')
        
    else:
        form=VideoCreateForm()
        
    context={
        'form': form,
    }
    
    return render(request,'channel/upload_video.html',context)
    


