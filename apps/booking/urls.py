from django.urls import path

from booking.views import booking

app_name = 'booking'

urlpatterns = [
    path('reservation/<pk>', booking, name="reservation"),

]
