from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=250)
    height=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class PrefPopulation(models.Model):
    name=models.CharField(max_length=250)
    sex=models.IntegerField()
    population=models.IntegerField()
    

class SomeTable(models.Model):
    name=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
