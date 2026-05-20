from django.db import models

# Create your models here.
class clients(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)