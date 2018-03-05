from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

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
        return self.email

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

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.owner.username

@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
	if created:
		user_profile, created = UserProfile.objects.get_or_create(owner=instance)
