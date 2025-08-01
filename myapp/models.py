from django.db import models

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