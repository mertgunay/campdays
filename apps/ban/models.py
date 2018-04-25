from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class BannedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=255)


    def __str__(self):
        return self.user.get_full_name()
