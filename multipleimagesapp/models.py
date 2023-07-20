from django.db import models

# Create your models here.
class Gallery(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=50,default="No Title",blank=True)
    images = models.TextField(blank=True)