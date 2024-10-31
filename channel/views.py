from django.shortcuts import get_object_or_404, redirect, render

from channel.forms import VideoCreateForm
from channel.models import Channel
from core.models import  Video
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def channel_profile(request,channel_name):
    channel = get_object_or_404(Channel,id=channel_name)
    videos=Video.objects.filter(user=channel.user,visibility='public').order_by('-views')
    
    try:
        video_featured=Video.objects.get(featured=True,user=channel.user.id)
    except:
        video_featured = None
        messages.warning(request,f'Only one video can featured!')
    
    context={
        'channel': channel,
        'videos': videos,
        'video_featured': video_featured,
    }
    return render(request,'channel/channel.html',context)



def channel_videos(request,channel_name):
    channel = get_object_or_404(Channel,id=channel_name)
    videos=Video.objects.filter(user=channel.user,visibility='public').order_by('-date')
    
    
    
    context={
        'channel': channel,
        'videos': videos,
    }
    
    return render(request,'channel/channel_videos.html',context)


def channel_about(request,channel_name):
    channel = get_object_or_404(Channel,id=channel_name)
    videos=Video.objects.filter(user=channel.user,visibility='public').order_by('-date')
    
    
    
    context={
        'channel': channel,
        'videos': videos,
    }
    
    return render(request,'channel/channel_about.html')
    
    



# video-upload
@login_required
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
    


@login_required
def video_edit(request,video_id,channel_id):
    user=request.user
    video=Video.objects.get(id=video_id)
    channel=Channel.objects.get(id=channel_id)
    
    if request.method=='POST':
        form=VideoCreateForm(request.POST,request.FILES,instance=video)
        
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=user
            new_form.save()
            form.save_m2m()
            messages.success(request,f'Video Editted successfully')
            return redirect('index')
        
    else:
        form=VideoCreateForm(instance=video)
        
    context={
        'form': form,
        'video': video,
    }
    
    return render(request,'channel/upload_video.html',context)

