from django.db import models
from django.utils import timezone
from datetime import date


class Blog( models.Model):
    title   = models.CharField(max_length=200)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=False, auto_now =False,null=True,blank=True)

    def __str__(self):
        return self.title

