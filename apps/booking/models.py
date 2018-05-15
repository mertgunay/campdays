from django.db import models
from django.contrib.auth import get_user_model
from campowner.models import CampOwner

User = get_user_model()




class Reservation(models.Model):

    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    #place        = models.ForeignKey()
    #check_in     = models.DateField(default=datetime.today)
    #check_out    = models.DateField(default=datetime.tomorrow)
    guest        = models.IntegerField(default=1)
    price        = models.IntegerField(default=0)


    def __str__(self):
        return self.place
