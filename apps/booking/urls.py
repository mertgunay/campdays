from django.urls import path

from booking.views import booking, list_reservations

app_name = 'booking'

urlpatterns = [
    path('reservation/<pk>', booking, name="reservation"),
    path('list_reservations', list_reservations, name='list_reservations'),

]
