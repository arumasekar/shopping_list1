from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    description = models.TextField()
    price = models.IntegerField() 
    size = models.CharField(max_length=255, default=" ")

def __str__(self) -> str:
        return self.name