from django.shortcuts import render
from .models import *

def home(request):
    catgor=request.GET.get('catgor')
    if catgor==None:
        posts=Post.objects.all()
    else:
        posts=Post.objects.filter(tanlov__nomi=catgor)
    catgories=Catagory.objects.all()
    context={
        'posts':posts,
        'catgories':catgories
    }  
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')