from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from utils.slugify import unique_slug_generator

User = get_user_model()

def campowner_upload_location(instance, filename):
	return "campowners/%s/%s" %(instance.slug, filename)

class CampOwner(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    name            = models.CharField(max_length=50)
    slug            = models.SlugField(unique=True, blank=True)
    address         = models.CharField(max_length=255)
    image           = models.ImageField(
        upload_to=campowner_upload_location,
        width_field='width_field',
        height_field='height_field',
        null=True,
        blank=True,
    )
    width_field     = models.PositiveIntegerField(default=0)
    height_field    = models.PositiveIntegerField(default=0)
    is_active       = models.BooleanField(default=False)

    def __str__(self):
    	return self.name

@receiver(pre_save, sender=CampOwner)
def campowner_pre_save_receiver(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)
