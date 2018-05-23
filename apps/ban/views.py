from django.shortcuts import render
from django.contrib.auth import get_user_model
from ban.models import BannedUser
import datetime

User = get_user_model()


def stat(request):
    queryset = BannedUser.objects.all()
    date_from = datetime.datetime.now() - datetime.timedelta(hours=1)
    last_logins = User.objects.filter(last_login__gte=date_from)
    context = {
        'banned_users': queryset,
        'object_list': last_logins,
    }
    return render(request, "ban/stat.html", context)
