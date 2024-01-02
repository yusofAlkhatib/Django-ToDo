from django.db import models
from django.utils import timezone

# Create your models here.


class ToDo(models.Model):
    name = models.CharField(max_length=50)
    creatrd_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100)
    