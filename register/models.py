from django.db import models

# Create your models here.



class Doner(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    bloodgroup = models.CharField(max_length=15)
    phno = models.CharField(max_length=15)
