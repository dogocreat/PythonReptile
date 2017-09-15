from django.shortcuts import render

#import HttpResponse
from django.http import HttpResponse

#import render need datatime and shortcuts
from datetime import datetime

#import models
from .models import Post

# Create your views here.

def hello_world(request):
	return render(request,'hello_world.html',{
		'current_time':str(datetime.now()),
	})
#	return HttpResponse("Hello World!")

def home(request):
	post_list = Post.objects.all()
	return render(request,'home.html',{
		'post_list': post_list,
	})
	
def post_detail(request,pk):
	post = Post.objects.get(pk=pk)
	return render(request,'post.html',{
		'post': post,
	})

def add_post(request):
	author = 'dogocreat'
	return render(request,'add_post.html',{
		'author': author,
	})

def edit_post(request,pk):
    post_detail = Post.objects.get(pk=pk)
    return render(request,'edit_post.html',{
		'post_detail': post_detail
	})
	