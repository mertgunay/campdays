
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager
from utils.choices import GENDER_CHOICES

def users_upload_location(instance, filename):
	return "users/%s/%s" %(instance.username, filename)

class User(AbstractBaseUser, PermissionsMixin):
	username_validator = UnicodeUsernameValidator()

	image            = models.ImageField(upload_to=users_upload_location,
	    width_field ='width_field',
	    height_field='height_field',
	    null=True,
	    blank=True,
	)
	width_field     = models.PositiveIntegerField(
		null=True,
	    blank=True,
		default=0
	)

	height_field    = models.PositiveIntegerField(
		null=True,
	    blank=True,
		default=0
	)

	gender		    = models.CharField(
		_('Cinsiyet'),
		max_length=10,
		choices=GENDER_CHOICES
	)

	username        = models.CharField(
	    _('username'),
	    max_length=150,
	    unique=True,
	    validators=[username_validator],
	    error_messages={
	        'unique': _("Bu kullanıcı adı mevcut"),
	    },
	)
	email           = models.EmailField(
	    _('E-posta'),
	    max_length=255,
	    unique=True
	)
	first_name      = models.CharField(
	    _('İsim'),
	    max_length=50,
	    blank=True
	)
	last_name       = models.CharField(
	    _('Soyisim'),
	    max_length=50,
	    blank=True
	)
	is_active       = models.BooleanField(
	    _('active'),
	    default=True,
	    help_text=_(
	        'Designates whether this user should be treated as active.'
	        ' Unselect this instead of deleting accounts.'
	    ),
	)
	is_staff        = models.BooleanField(
	    _('staff status'),
	    default=False,
	    help_text=_(
	        'Designates whether the user can log into this admin site.'
	    ),
	)
	timestamp       = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	class Meta:
	    verbose_name = _('user')
	    verbose_name_plural = _('users')

	def __str__(self):
	    return self.get_full_name()

	def get_absolute_url(self):
	    return reverse('users:user_detail', kwargs={'username': self.username})

	def get_full_name(self):
		"""
		Return the first_name plus the last_name, with a space in between.
		"""
		full_name = '%s %s' % (self.first_name, self.last_name)
		if not full_name.strip():
			full_name = self.username
		return full_name.strip()

	def get_short_name(self):
		"""Return the short name for the user."""
		first_name = self.first_name
		if not first_name:
			first_name = self.username
		return first_name

	def get_image_url(self):
		url = None
		if self.image:
			url = self.image.url
		else:
			if self.gender == 'male':
				url = settings.STATIC_URL + 'default/img/user-male.png'
			else:
				url = settings.STATIC_URL + 'default/img/user-female.png'
		print(url)
		return url

	def email_user(self, subject, message, from_email=None):
	    """
	    Sends an email to this User.
	    """
	    send_mail(subject, message, from_email, [self.email])
