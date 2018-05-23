from django.db import models
from django.contrib.auth import get_user_model
from campowner.models import CampOwner
from camps.models import campLocation
import datetime
User = get_user_model()

class Reservation(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    place        = models.ForeignKey(campLocation, on_delete=models.CASCADE)
    check_in     = models.DateField(default=datetime.date.today)
    check_out    = models.DateField(default=datetime.date.today)
    guests       = models.IntegerField(default=1)
    tents        = models.IntegerField(default=1) 
    timestamp    = models.DateTimeField(auto_now_add=True)
