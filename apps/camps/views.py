from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.contrib.auth import  authenticate, login, logout, update_session_auth_hash
# from django.urls import reverse
from .forms import createAreaForm
from .models import campLocation
from campowner.forms import CampOwnerRegisterForm
from campowner.models import CampOwner, BlockedPosts
from blog.models import Post
# Create your views here.




def index(request):

    return render(request, "index.html")

def home(request):

    return render(request, "home.html")


def maps(request):

    locs=campLocation.objects.all()

    return render(request, "maps.html",{'locs':locs})


def createCampingArea(request):
    campowners = CampOwner.objects.filter(user=request.user)
    if not campowners:
        return HttpResponseRedirect("/camps/maps")

    if request.method == 'POST':
        form = createAreaForm(request.POST)
        if form.is_valid():
            creator=request.user.campowner
            campLocation=form.save(commit=False)
            campLocation.creator = creator
            campLocation.lat = form.cleaned_data['lat']
            campLocation.lon = form.cleaned_data['lng']
            campLocation.name = form.cleaned_data['name']
            campLocation.title = form.cleaned_data['title']
            campLocation.description = form.cleaned_data['description']
            campLocation.max_guests = form.cleaned_data['max_guests']
            campLocation.max_tents = form.cleaned_data['max_tents']
            campLocation.rating = 50
            campLocation.save()
            return redirect('../maps')

    form = createAreaForm()
    return render(request, 'addCampArea.html', {'form': form})



def filter(request):

    return render(request, "filter.html")

def detail(request, id):
    campId = id
    camp = campLocation.objects.get(id=id)
    obj = get_object_or_404(CampOwner, pk=id)
    blogs = Post.objects.filter(user=obj.user)
    context = {
        'campowner': obj,
        'object_list': blogs,
    }

    return render(request, "camp.html", {'camp' : camp ,'context' : context})


# def createCampingArea(request):

#     locs=campLocation.objects.all()

#     return render(request, "addCampArea.html",{'locs':locs})


# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()

#             return redirect('../home')
#     else:
#         form = SignUpForm()
#     return render(request, 'register.html', {'form': form})

# def logout_request(request):
#     logout(request)
#     return HttpResponseRedirect('../login')

# def login_request(request):

#     if request.method == 'POST':
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             print('here')
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('../index')
#     form = LoginForm()
#     context = {'form': form}
#     return render(request, 'login.html', context)
