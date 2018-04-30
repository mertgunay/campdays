from django.urls import path
from ban.views import stat
app_name = 'ban'

urlpatterns = [
    path('stat/', stat, name="stat"),

]
