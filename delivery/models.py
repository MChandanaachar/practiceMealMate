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
    picture=models.URLField(max_length=500,default="https://cdn4.vectorstock.com/i/1000x1000/65/58/restaurant-logo-design-idea-vector-46986558.jpg")
    cuisine=models.CharField(max_length=200)
    rating=models.FloatField()

class Item(models.Model):
    # when delete restaurant i have to delete respective menu also so cascade helps to on edelete another also delete for that i use foriegn key
    Restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    picture=models.URLField(max_length=200, default="https://cdn-icons-png.flaticon.com/512/1147/1147856.png")
    description=models.CharField(max_length=200)
    price=models.FloatField()
    is_veg=models.BooleanField(default=True)
