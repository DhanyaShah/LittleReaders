from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    images = ArrayField(models.CharField(max_length = 100), blank = True)
    audiofiles = ArrayField(models.CharField(max_length = 100), blank = True)
    length = models.IntegerField()
