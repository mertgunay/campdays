from django.shortcuts import render
from ban.models import BannedUser
# Create your views here.

def stat(request):
    queryset = BannedUser.objects.all()
    context = {
        'banned_users': queryset,
    }
    return render(request, "ban/stat.html", context)
