from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def index(request):
    blogs = Blog.objects
    return render(request, 'index.html',{'blogs': blogs})

def detail(request, blog_id):
    blogs_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog_detail': blogs_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.content = request.GET['content']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/'+str(blog.id))

def destroy(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    return redirect('/')
