from django.shortcuts import render

from core.models import Comment, Video
from django.contrib.auth.decorators import login_required



@login_required
def studio(request):
    user=request.user
    videos=Video.objects.filter(user=user).order_by('-date')
    channel=user.channel
    comments=Comment.objects.filter()
    
    context={
        'user': user,
        'videos': videos,
        'channel': channel,
    }
    return render(request,'useradmin/studio.html',context)