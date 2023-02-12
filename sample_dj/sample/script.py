from sample.models import Student
from datetime import datetime

Student.objects.create(department="a",submitted_at=None)
Student.objects.create(department="a",submitted_at=datetime(year=2023,month=3,day=3))
Student.objects.create(department="b",submitted_at=datetime.now())
Student.objects.create(department="b",submitted_at=datetime.now())
Student.objects.create(department="c",submitted_at=datetime(year=2023,month=3,day=3))
Student.objects.create(department="c",submitted_at=datetime.now())


from models  import Item,Shop

beer=Item.objects.create(name="beer")

Item.objects.all()


bicycle=Item.objects.create(name="bicycle")

car=Item.objects.create(name="car")
Shop.objects.create(name="sendai",item="beer")
Shop.objects.create(name="sendai",item="car")
Shop.objects.create(name="sendai",item="bicycle")

Shop.objects.create(name="osaka",item="beer")



class Prc(models.Model):s
    prc_date=models.DateTimeField()
    amount=models.IntegerField()


Prc.objects.create(prc_date=datetime(2018,10,11),amount=1200)
Prc.objects.create(prc_date=datetime(2018,10,12),amount=3999)
Prc.objects.create(prc_date=datetime(2018,10,14),amount=3200)
Prc.objects.create(prc_date=datetime(2018,10,15),amount=-999)
Prc.objects.create(prc_date=datetime(2018,10,17),amount=1200)
Prc.objects.create(prc_date=datetime(2018,10,18),amount=299)
Prc.objects.create(prc_date=datetime(2018,10,19),amount=299)

'''
class Purchase(models.Model):
    cust_id=models.CharField(max_length=10)
    price=models.IntegerField

'''
from random import randint
for i in ["A","B","C","D"]:
    for  j in range(20):
        Purchase.objects.create(cust_id=i,price=randint(1,100))
