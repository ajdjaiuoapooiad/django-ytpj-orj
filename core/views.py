from django.shortcuts import render

from core.models import Comment, Video



def index(req):
    videos = Video.objects.all()
    
    context = {
        'videos': videos,
    }
    return render(req,'index.html',context)



def detail(req,pk):
    video = Video.objects.get(id=pk)
    videos = Video.objects.all()
    comments=Comment.objects.filter(video=video,active=True).order_by('-date')
    
    context = {
        'video': video,
        'videos':videos,
        'comments': comments,
    }
    return render(req,'detail.html',context)

def create(req):
    return render(req,'create.html')

def update(req):
    return render(req,'update.html')


