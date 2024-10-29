from django.shortcuts import render



def index(req):
    return render(req,'index.html')

def detail(req):
    return render(req,'detail.html')

def create(req):
    return render(req,'create.html')

def update(req):
    return render(req,'update.html')


