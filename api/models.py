from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Netflix(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    series= models.CharField(max_length=64,blank=True)
    movie= models.CharField(max_length=64,blank=True)
    episode= models.CharField(max_length=64,blank=True)
    season= models.CharField(max_length=64,blank=True)

    def __str__(self):
        return f"{self.user}   {self.movie}   {self.series}"