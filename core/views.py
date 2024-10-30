from django.shortcuts import render

from core.models import Video



def index(req):
    videos = Video.objects.all()
    
    context = {
        'videos': videos,
    }
    return render(req,'index.html',context)



def detail(req,pk):
    video = Video.objects.get(id=pk)
    
    context = {
        'video': video,
    }
    return render(req,'detail.html',context)

def create(req):
    return render(req,'create.html')

def update(req):
    return render(req,'update.html')


