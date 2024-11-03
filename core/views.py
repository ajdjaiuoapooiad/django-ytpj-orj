from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from channel.models import Channel
from core.models import Comment, Video
from django.views.decorators.csrf import csrf_exempt



def index(req):
    videos = Video.objects.filter(visibility='public')
    
    context = {
        'videos': videos,
    }
    return render(req,'index.html',context)



def detail(req,pk):
    video = Video.objects.get(id=pk)
    videos = Video.objects.filter(visibility='public').order_by('-views')
    comments=Comment.objects.filter(video=video,active=True).order_by('-date')
    channel=Channel.objects.get(user=video.user)
    
    video.views += 1
    video.save()
    
    channel.total_view += 1
    channel.save()
    
    context = {
        'video': video,
        'videos':videos,
        'comments': comments,
        'channel': channel,
    }
    return render(req,'detail.html',context)

def create(req):
    return render(req,'create.html')

def update(req):
    return render(req,'update.html')




# Ajax
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
    
    
def load_sub(request,id):
    subscribers=Video.objects.get(id=id)
    sub_lists=list(subscribers.subscribers.value())
    return JsonResponse(sub_lists,safe=False,status=200)
    
    
    
    