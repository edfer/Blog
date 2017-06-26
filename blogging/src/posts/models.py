from django.conf import settings
from django.db import models

# Create your models here.

from .validators import content_validation

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    content = models.TextField(validators=[content_validation])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.title)
