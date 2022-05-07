from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Customer)
class CustomerRegister(admin.ModelAdmin):
    list_display = ('user','name', 'phone', 'email')

@admin.register(Product)
class ProductRegister(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

@admin.register(Order)
class OrderRegister(admin.ModelAdmin):
    list_display = ('customer', 'product', 'status')

@admin.register(Tag)
class TagRegister(admin.ModelAdmin):
    list_display=('name',)