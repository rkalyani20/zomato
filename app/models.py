from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=40,unique=True)
    phone_no = models.CharField(max_length=40,blank=True)

    def __str__(self):
        return self.username

class Restaurant(models.Model):
    name= models.CharField(max_length=40)
    contact= models.CharField(max_length=40)
    address= models.CharField(max_length=40)


    def __str__(self):  
        return self.name

class Menu(models.Model):
    restaurant_name= models.ForeignKey(Restaurant, on_delete= CASCADE)
    items= models.CharField(max_length=40)
    price= models.IntegerField()

class Order(models.Model):
    user_name= models.CharField( max_length=40)
    user_contact= models.CharField(max_length=40)
    user_email= models.EmailField(max_length=40)
    user_address=models.CharField(max_length=40)
    item_name= models.CharField(max_length=40, default= None)
    restaurant_name= models.CharField(max_length=40)

    

