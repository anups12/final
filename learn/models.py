from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True)
    pic = models.ImageField(null=True, default='avatar.png')
    email = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('indoor','indoor'),
        ('out door','out door'),
    )
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=6 )
    category = models.CharField(max_length=100, null=True, choices=CATEGORY )
    description = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)
