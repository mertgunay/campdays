from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
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
