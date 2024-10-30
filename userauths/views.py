from django.shortcuts import redirect, render
from django.contrib import messages
from ytpj import settings
from django.contrib.auth import login,authenticate

User=settings.AUTH_USER_MODEL


def registerView(req):
    return render(req,'userauths/register.html')

def loginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            user=User.request.get('email')
        except:
            messages.warning(request,'user does not exist')
            
        user=authenticate(request,email=email,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,'You are logged in')
            return redirect('index')
        else:
            messages.warning(request,'Email or Password , does not exist')
    
    
    return render(request,'userauths/login.html')

def logoutView(req):
    return render(req,'userauths/login.html')

