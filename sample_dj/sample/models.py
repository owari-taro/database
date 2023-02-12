from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PrefPopulation(models.Model):
    name = models.CharField(max_length=250)
    sex = models.IntegerField()
    population = models.IntegerField()
    4


class SomeTable(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class Status(models.TextChoices):
    """_summary_

    :param _type_ models: _description_
    """

    finished = "finished"
    waiting = "waiting"


class Project(models.Model):
    """_summary_

    :param _type_ models: _description_
    """

    pid = models.CharField(max_length=250)
    step_num = models.IntegerField()
    status = models.CharField(choices=Status.choices, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["pid", "step_num"], name="lesson_unique"),
            models.CheckConstraint(
                name="%(class)s_status_check",
                check=models.Q(status__in=Status.values),
            ),
        ]




class Person(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250,null=True)

    

class SeqTbl(models.Model):
    seq=models.IntegerField()
    name=models.CharField(max_length=250)


class Student(models.Model):
    department=models.CharField(max_length=100)
    submitted_at=models.DateTimeField(null=True)


class Item(models.Model):
    name=models.CharField(max_length=250,unique=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)

class Shop(models.Model):
    name=models.CharField(max_length=250)
    item=models.CharField(max_length=250)


class Prc(models.Model):
    prc_date=models.DateTimeField()
    amount=models.IntegerField()





class Purchase(models.Model):
    cust_id=models.CharField(max_length=10)
    price=models.IntegerField(default=0)


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    