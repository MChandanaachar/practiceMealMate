from django.db import models

# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=50)

class Restaurant(models.Model):
    name=models.CharField(max_length=20)
    picture=models.CharField(max_length=500,default="https://cdn4.vectorstock.com/i/1000x1000/65/58/restaurant-logo-design-idea-vector-46986558.jpg")
    cuisine=models.CharField(max_length=200)
    rating=models.FloatField()