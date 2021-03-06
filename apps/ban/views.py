from django.shortcuts import render
from django.contrib.auth import get_user_model
from ban.models import BannedUser
from booking.models import Reservation
from camps.models import campLocation
import datetime

User = get_user_model()


def stat(request):
    queryset = BannedUser.objects.all()
    date_from = datetime.datetime.now() - datetime.timedelta(hours=1)
    last_logins = User.objects.filter(last_login__gte=date_from)
    reservation_list = Reservation.objects.filter(timestamp__gte=date_from)
    camp_areas = campLocation.objects.filter(dateCreated__gte=date_from)
    context = {
        'banned_users': queryset,
        'object_list': last_logins,
        'reservation_list': reservation_list,
        'camps_areas': camp_areas,
    }
    return render(request, "ban/stat.html", context)
