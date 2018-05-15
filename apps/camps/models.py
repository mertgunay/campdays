from django.db import models
from django.contrib.auth import get_user_model
from campowner.models import CampOwner
# Create your models here.

User = get_user_model()

# class Location(models.Model):
#     creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'creator')
#     lat  = models.DecimalField(max_digits=9, decimal_places=6)
#     lng = models.DecimalField(max_digits=9, decimal_places=6)
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=20)
#     description = models.CharField(max_length=100, default='')
#     rating = models.PositiveIntegerField(range(1, 100))
#     dateCreated=models.DateTimeField(auto_now=True, editable=False)

#     class Meta:
#         db_table = u'Location'

#     def __str__(self):
#         return self.title


class campLocation(models.Model):
    creator = models.ForeignKey(CampOwner, on_delete=models.CASCADE, related_name = 'creator')
    lat  = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, default='')
    rating = models.PositiveIntegerField(range(1, 100))
    dateCreated=models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = u'campLocation'

    def __str__(self):
        return self.title
