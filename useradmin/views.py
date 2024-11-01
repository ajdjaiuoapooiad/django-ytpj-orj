from django.shortcuts import render

from core.models import Video




def studio(request):
    videos=Video.objects.filter(user=request.user).order_by('-date')
    
    context={
        'videos': videos,
    }
    return render(request,'useradmin/studio.html',context)