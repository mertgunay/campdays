from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.translation import gettext, gettext_lazy as _

from utils.slugify import unique_slug_generator

User = get_user_model()

def campowner_upload_location(instance, filename):
	return "campowners/%s/%s" %(instance.slug, filename)

class CampOwner(models.Model):
	user            = models.OneToOneField(User, on_delete=models.CASCADE)
	name            = models.CharField(
		_('Kamp Alanı Adı'),
		max_length=50,
	)
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
	is_pending 		= models.BooleanField(default=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	desc 			= models.CharField(max_length=255, blank=True, null=True)
	phone_number 	= models.CharField(max_length=100)
	web_site 		= models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name

class CampProfile(models.Model):
    owner = models.OneToOneField(CampOwner, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)

    def __str__(self):
        return self.owner.name

@receiver(post_save, sender=CampOwner)
def camp_post_save_receiver(sender, instance, created, *args, **kwargs):
	if created:
		camp_profile, created = CampProfile.objects.get_or_create(owner=instance)

@receiver(pre_save, sender=CampOwner)
def campowner_pre_save_receiver(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)
