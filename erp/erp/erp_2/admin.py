from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'grade', 'tel',)
    search_fields = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'basic_price',)
    search_fields = ('id',)


@admin.register(Order2)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'salesman', 'price', 'amount', 'date', 'deliver2', 'payment',)
    search_fields = ('id',)