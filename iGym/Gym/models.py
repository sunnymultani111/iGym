from django.db import models
from django.urls import reverse

# Create your models here.


class Trainee(models.Model):
    name = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=400, default="")
    city = models.CharField(max_length=400, default="")
    state = models.CharField(max_length=400, default="")
    zip_code = models.CharField(max_length=400, default="")

    def __str__(self):
        return self.name + "-" + self.city

    def get_absolute_url(self):
        return reverse('Gym:trainee-detail', kwargs={'pk': self.pk})
