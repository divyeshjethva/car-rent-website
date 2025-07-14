from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name}"