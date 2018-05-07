from django.contrib import admin
from .models import campLocation

# Register your models here.

class campLocationsModelAdmin(admin.ModelAdmin):
    list_display = ["name","title","lat", "lng","creator","description","rating"]
    list_filter = ["name","title","lat", "lng","creator","description","rating"]
    search_fields = ["title"]
admin.site.register(campLocation, campLocationsModelAdmin)
