from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from channel.forms import ChannelEditForm, CommunityCreateForm, VideoCreateForm
from channel.models import Channel, Community, CommunityComment
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
        # messages.warning(request,f'Only one video can featured!')
    
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



def channel_community(request,channel_name):
    channel = get_object_or_404(Channel,id=channel_name)
    community = Community.objects.filter(channel=channel,status='Active').order_by('-date')
    
    context={
        'channel': channel,
        'community': community,
    }
    return render(request,'channel/channel_community.html',context)

   
   
   
   
   
def channel_community_detail(request,channel_name,community_id):
    channel = get_object_or_404(Channel,id=channel_name)
    community = Community.objects.get(channel=channel,status='Active',id=community_id)
    comments=CommunityComment.objects.filter(community=community,active=True).order_by('-date')
    
    
    context={
        'channel': channel,
        'community':community,
        'comments': comments,
    }
    return render(request,'channel/channel_community_detail.html',context)

 
 


# Create-post
@login_required
def create_community_post(request,channel_id):
    user=request.user
    channel=Channel.objects.get(id=channel_id)
    
    if request.method == 'POST':
        form=CommunityCreateForm(request.POST,request.FILES)
        
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.channel=channel
            new_form.save()
            messages.success(request,'Community created successfully!')
            return redirect('channel-community',channel.id)
    else:
        form=CommunityCreateForm()
        
    context={
        'form': form,
    }
            
            
    return render(request,'channel/create-post.html',context)
 
 
def edit_community_post(request,channel_id,community_post_id):
    community=Community.objects.get(id=community_post_id)   #ここを変更したい
    user=request.user
    channel=Channel.objects.get(id=channel_id)
     
     
    if request.method == 'POST':
        form=CommunityCreateForm(request.POST,request.FILES,instance=community)
        
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.channel=channel
            new_form.save()
            messages.success(request,'Community editted successfully!')
            return redirect('channel-community',channel.id)
    else:
        form=CommunityCreateForm(instance=community)
        
    context={
        'form': form,
    }
            
            
    return render(request,'channel/create-post.html',context)
                    




def delete_community_post(request,channel_id,community_post_id):
    community=Community.objects.get(id=community_post_id)   #ここを変更したい
    user=request.user
    channel=Channel.objects.get(id=channel_id)
     
    community.delete()
    messages.success(request,f'Community deleted successfully!')
    return redirect('channel-community',channel.id)
    
 
 
 
 

 
 
 
 
#  Create-Comment
@login_required
def create_comment(request,community_id):
    
    if request.method == 'POST':
        community=Community.objects.get(id=community_id,status='Active')
        comment=request.POST.get('comment')
        user=request.user
        
        new_comment=CommunityComment.objects.create(comment=comment,user=user,community=community)
        new_comment.save()
        messages.success(request,f'Comment created successfully!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
 
def delete_comment(request,community_id,comment_id):
    community=Community.objects.get(id=community_id)
    comment=CommunityComment.objects.get(id=comment_id)
    
    
    comment.delete()
    messages.success(request,f'Comment deleted successfully!')
    return redirect('channel-community-detail',community.channel.id,community.id)
 
  
# Likes
@login_required
def add_new_like(request,community_id):
    community=Community.objects.get(id=community_id)
    user=request.user
    
    if user in community.likes.all():
        community.likes.remove(user)
    else:
        community.likes.add(user)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    




    
def channel_about(request,channel_name):
    channel=get_object_or_404(Channel,id=channel_name)
    
    
    context={
        'channel': channel,
    }
    
    
    return render(request,'channel/channel_about.html',context)






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
def video_edit(request,channel_id,video_id):
    video=Video.objects.get(id=video_id)
    channel=Channel.objects.get(id=channel_id)
    user=request.user
    
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


@login_required
def video_delete(request,video_id):
    video=Video.objects.get(id=video_id)
    user=request.user
    
    if request.user==video.user:
        video.delete()
        messages.success(request,f'Video deleted successfully!')
        return redirect('index')
    else:
        return HttpResponse('You are not allowed to delete this video')




def edit_channel(request,channel_id):
    user=request.user
    channel=Channel.objects.get(id=channel_id)
    
    if request.method == 'POST':
        form=ChannelEditForm(request.POST,request.FILES,instance=channel)
        
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.channel=channel
            new_form.save()
            messages.success(request,'Community editted successfully!')
            return redirect('channel-profile',channel.id)
    else:
        form=ChannelEditForm(instance=channel)
        
    context={
        'form': form,
        'channel':channel,
    }
            
            
    return render(request,'channel/channe_edit.html',context)



