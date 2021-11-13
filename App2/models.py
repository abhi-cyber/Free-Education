from django.db import models



# Create your models here.
class employe(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    status = models.BooleanField()
    salary = models.IntegerField()