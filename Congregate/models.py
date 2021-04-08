from django.db import models
from django.utils import timezone

# Create your models here.

class Content_Model(models.Model):
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    url = models.URLField()
    
# class BBC_Model(models.Model):
#     source = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     title = models.CharField(max_length=500)
#     url = models.URLField()
#     # time = models.DateTimeField(default=timezone.now)

# class Medium_Model(models.Model):
#     source = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     title = models.CharField(max_length=500)
#     url = models.URLField()
#     # time = models.DateTimeField(default=timezone.now)

# class Engadget_Model(models.Model):
#     source = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     title = models.CharField(max_length=500)
#     url = models.URLField()
#     # time = models.DateTimeField(default=timezone.now)
    
# class Byteiota_Model(models.Model):
#     source = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     title = models.CharField(max_length=500)
#     url = models.URLField()
    # time = models.DateTimeField(default=timezone.now)