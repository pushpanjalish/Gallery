from django.db import models

# Create your models here.
class Gallery(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField()