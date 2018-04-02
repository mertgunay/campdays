from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages

from .forms import PostForm
from .models import Post

# Create your views here.

def blog_create(request):

    if not request.user.is_authenticated:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
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

    queryset_list = Post.objects.all() #.order_by("-timestampt")

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
                ).distinct()

    paginator = Paginator(queryset_list, 5) # Show 10 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
    }

    return render(request, "post_list.html", context)

def blog_update(request, id=None):

    if not request.user.is_authenticated:
        raise Http404

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
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
