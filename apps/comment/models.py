from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
# Create your models here.

from blog.models import Post

User = get_user_model()

class CommentManager(models.Manager):
    def filter_by_instance(self, instance):

        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)

        return qs

class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    objects = CommentManager()

    def __unicode__(self):
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)
