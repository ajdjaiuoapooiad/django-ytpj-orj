from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from userauths.forms import UserRegisterForm
from ytpj import settings
from django.contrib.auth import login,authenticate,logout

User=settings.AUTH_USER_MODEL


def registerView(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method=='POST':
        form=UserRegisterForm(request.POST or None)
        
        try:
            if form.is_valid():
                new_user=form.save()
                username=form.cleaned_data.get('username')
                messages.success(request,f'Hey {username}, Account Created')
                new_user=authenticate(
                    username=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'],
                    )
                login(request,new_user)
                return redirect('index')
        except:
            messages.error(request,f'An error has occurred')
    else:
        form=UserRegisterForm()
        
    context={
        'form':form,
    }  
    
    return render(request,'userauths/register.html',context)

def loginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            user=User.request.get('email')
        except:
            user=None
            # messages.warning(request,'user does not exist')
            
        user=authenticate(request,email=email,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,f'Hey "{user}", You are logged in')
            return redirect('index')
        else:
            messages.warning(request,'Email or Password , does not exist')
    
    
    
    return render(request,'userauths/login.html')

def logoutView(request):
    logout(request)
    messages.success(request,'You are logged out')
    return redirect('sign-in')

