#from django.conf import settings
from django.urls import reverse
from django.db import models


# Create your models here.

def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):

    #user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestampt = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("blog:blog_detail", kwargs={"id": self.id})
        #return "/blog/%s/" %(self.id)

    class Meta:
        ordering = ["-timestampt", "-updated"]
