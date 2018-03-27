from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def blog_home(request):
    return HttpResponse("<h1>Hello There</h1>")

def blog_detail(request, id=None):

    instance = get_object_or_404(Post, id=1)
    context = {
    "title": instance.title,
    "instance": instance,
    }

    return render(request, "detail.html", context)

def blog_list(request):

    queryset = Post.objects.all()
    context = {
    "object_list": queryset,
    "title": "List"
    }

    return render(request, "blog.html", context)

def blog_update(request):
    return HttpResponse("<h1>Update</h1>")

def blog_delete(request):
    return HttpResponse("<h1>Delete</h1>")
