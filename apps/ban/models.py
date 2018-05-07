from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class BannedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        self.user.is_active = False
        self.user.save()
        super().save(*args, **kwargs)
