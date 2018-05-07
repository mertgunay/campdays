from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from camps import views as camp_views

from camps.views import home, maps, createCampingArea, filter 

app_name = 'camps'

urlpatterns = [        
    url(r'^home/', camp_views.home),
    url(r'^maps/', camp_views.maps),
    url(r'^create/', camp_views.createCampingArea),
    url(r'^filter/', camp_views.filter),
]


