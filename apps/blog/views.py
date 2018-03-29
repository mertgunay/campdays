from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import PostForm
from .models import Post

# Create your views here.

def blog_create(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.error(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolut_url())

    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def blog_detail(request, id=None):

    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, "post_detail.html", context)

def blog_list(request):

    queryset = Post.objects.all().order_by("-timestampt")
    context = {
        "object_list": queryset,
        "title": "List"
    }

    return render(request, "post_list.html", context)

def blog_update(request, id=None):

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.error(request, "Post Updated")
        return HttpResponseRedirect(instance.get_absolut_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    return render(request, "post_form.html", context)

def blog_delete(request, id=None):

    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.error(request, "Post Deleted")
    return redirect("blog:list")
