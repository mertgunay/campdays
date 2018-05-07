from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth import  authenticate, login, logout, update_session_auth_hash
# from django.urls import reverse
from .forms import createAreaForm
from .models import campLocation
# Create your views here.




def index(request):
    
    return render(request, "index.html") 

def home(request):
    
    return render(request, "home.html")      


def maps(request):

    locs=campLocation.objects.all()
    
    return render(request, "maps.html",{'locs':locs})      


def createCampingArea(request):
    if request.method == 'POST':
        form = createAreaForm(request.POST)
        if form.is_valid():
            creator=request.user
            campLocation=form.save(commit=False)
            campLocation.creator = creator
            campLocation.lat = form.cleaned_data['lat']
            campLocation.lon = form.cleaned_data['lng']
            campLocation.name = form.cleaned_data['name']
            campLocation.title = form.cleaned_data['title']
            campLocation.description = form.cleaned_data['description']
            campLocation.rating = 50
            campLocation.save()
            return redirect('../maps')
    
    form = createAreaForm()
    return render(request, 'addCampArea.html', {'form': form})



def filter(request):
    
    return render(request, "filter.html") 

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