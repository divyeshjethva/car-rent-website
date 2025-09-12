from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=30)
    profile = models.ImageField(default="",upload_to="profile/")
    usertype = models.CharField(max_length=20,default="customer")
    
    def __str__(self):
        return f"{self.name}"

class Car(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = (
        ('Maruti','Maruti'),
        ('Mahindra','Mahindra'),
        ('Hyundai','Hyundai'),
    )
    
    cyear = models.IntegerField()
    compnaychoice = models.CharField(max_length=120,choices=company)
    cname = models.CharField(max_length=120)
    cprice = models.IntegerField()
    cimage = models.ImageField(default="",upload_to="car/")
    
    def __str__(self):
        return f"{self.cname},   {self.user}"

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    ttime = models.DateTimeField(default=timezone.now())

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    ttime = models.DateTimeField(default=timezone.now())
    total = models.IntegerField()
    qty = models.IntegerField(default=1)
    payment_status = models.BooleanField(default=False)