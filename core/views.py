from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render

from channel.models import Channel
from core.models import Comment, Video
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from userauths.models import Profile




@login_required
def index(request):
    videos = Video.objects.filter(visibility='public').order_by('-date')
    paginator=Paginator(videos,9)
    page=request.GET.get('page')
    paged_videos=paginator.get_page(page)
    
    context = {
        'videos': paged_videos,
    }
    return render(request,'core/index.html',context)


@login_required
def detail(request,pk):
    video = Video.objects.get(id=pk)
    videos = Video.objects.filter(visibility='public').order_by('-views')
    comments=Comment.objects.filter(video=video,active=True).order_by('-date')
    channel=Channel.objects.get(user=video.user)
    
    video.views += 1
    video.save()
    
    channel.total_view += 1
    channel.save()
    
    profile=request.user.profile
    profile.history_video.add(video)
    
    context = {
        'video': video,
        'videos':videos,
        'comments': comments,
        'channel': channel,
    }
    return render(request,'core/detail.html',context)






# Ajax
@login_required
def ajax_save_comment(request):
    if request.method == 'POST':
        pk=request.POST.get('id')
        
        comment=request.POST.get('comment')
        video=Video.objects.get(id=pk)
        user=request.user
        
        new_comment=Comment.objects.create(comment=comment,user=user,video=video)
        new_comment.save()
        
        response='Comment posted successfully!'
        return HttpResponse(response)
    
    

@csrf_exempt
def ajax_delete_comment(request):
    
    if request.method == 'POST':
        id=request.POST.get('cid')
        comment=Comment.objects.get(id=id)
        comment.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':2})
        


 
    
# Subscrive
@login_required
def add_new_sub(request,id):
    subscribers=Channel.objects.get(id=id)
    user=request.user
    
    if user in subscribers.subscribers.all():
        subscribers.subscribers.remove(user)
        response = 'Subscribe'
        return JsonResponse(response,safe=False,status=200)
    else:
        subscribers.subscribers.add(user)
        response = 'Unsubscribe'
        return JsonResponse(response,safe=False,status=200)
    

@login_required
def load_sub(request,id):
    subscribers=Channel.objects.get(id=id)
    sub_lists=list(subscribers.subscribers.values())
    return JsonResponse(sub_lists,safe=False,status=200)
    
    
    
# Likes
@login_required
def add_new_like(request,id):
    video=Video.objects.get(id=id)
    user=request.user
    
    if user in video.likes.all():
        video.likes.remove(user)
        like_response='<i class="fa fa-thumbs-up"></i>'
        return JsonResponse(like_response,safe=False,status=200)
    else:
        video.likes.add(user)
        like_response='<i class="fa fa-thumbs-up"></i>'
        return JsonResponse(like_response,safe=False,status=200)



@login_required
def load_like(request,id):
    video=Video.objects.get(id=id)
    like_lists=list(video.likes.values())
    return JsonResponse(like_lists,safe=False,status=200)
 

# Save-video
@login_required
def add_new_save(request,video_id):
    video=Video.objects.get(id=video_id)
    user=request.user.profile
    
    if video in user.save_video.all():
        user.save_video.remove(video)
    else:
        user.save_video.add(video)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        


# Search
@login_required
def searchView(request):
    video=Video.objects.filter(visibility='public').order_by('-views')
    query=request.GET.get('q')
    
    if query:
        video=video.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)
        ).distinct()
        
    context={
        'video': video,
        'query': query,
    }
    
    return render(request,'core/search.html',context)

  
  
@login_required
def tagView(request,tag_slug=None):
    video=Video.objects.filter(visibility='public').order_by('-views')
    tag=None
    
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        videos=video.filter(tags__in=[tag])
    
    
    context={
        'tag': tag,
        'videos': videos,
    }
    
    return render(request,'core/tags.html',context)        


# Save-video-index
@login_required
def save_video(request):
    user=request.user
    
    try:
        videos=user.profile.save_video.all()
    except:
        videos=None
        
    context={
        'videos': videos,
    }
    
    return render(request,'core/saved_video.html',context)


def like_video(request):
    user=request.user
    videos=Video.objects.filter(likes=user)
    
    context={
        'videos': videos,
    }
    
    return render(request,'core/saved_video.html',context)




def trend(request):
    videos = Video.objects.filter(visibility='public').order_by('-views')
    
    context = {
        'videos': videos,
    }
    return render(request,'core/index.html',context)



def subscribers(request):
    user=request.user
    channels=Channel.objects.filter(subscribers=user)

    
    context={
        'channels': channels,
        
    }
    
    return render(request,'channel/subscriber.html',context)




def history_video(request):
    user=request.user
    
    try:
        videos=user.profile.history_video.all().order_by('-date')
    except:
        videos=None
    
    context={
        'videos': videos,
    }
    
    return render(request,'core/saved_video.html',context)





