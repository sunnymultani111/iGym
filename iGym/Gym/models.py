from django.db import models

# Create your models here.
class Traniee(models.Model):
    name = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=400,default="")
    city = models.CharField(max_length=400,default="")
    state = models.CharField(max_length=400,default="")
    zip_code = models.CharField(max_length=400,default="")