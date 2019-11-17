from django.db import models

# Create your models here.
# from erp_1.models import *


class Supplier(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=10)
    contact = models.CharField (max_length=10, blank=True)
    number = models.CharField(max_length=20, blank=True)
    mail = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length= 20, blank=True)


def __str__(self):
    return self.name


class Supply(models.Model):
    material = models.ForeignKey('erp_1.Materials',null=True,on_delete=models.SET_NULL)
    supplier = models.ForeignKey('Supplier', null=True,on_delete=models.SET_NULL)
    price = models.FloatField(blank=True)
    tran_price = models.FloatField(blank=True)
    rate = models.FloatField(blank=True)


def __str__(self):
    return self.name


class Order(models.Model):
    supplier = models.ForeignKey('Supplier', null=True , on_delete=models.SET_NULL)
    staff = models.ForeignKey('erp_1.Staff', null=True ,on_delete=models.SET_NULL)
    id = models.CharField(max_length=6, primary_key=True)
    send_time = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=20, blank=True)
    order_maker = models.CharField(max_length=10, blank=True)
    reviewer = models.CharField(max_length=10, blank=True)
    predict_time = models.DateField(blank=True)
    remarks = models.CharField(max_length=100, blank=True)
    reality_time = models.DateField(blank=True,null=True)
    state = models.CharField(max_length=3, blank=True,default='未确认')
    trouble_order = models.BooleanField(default=0)
    credit_mark = models.FloatField(blank=True,null=True)
    quality_mark = models.FloatField(blank=True,null=True)
    operator = models.CharField(max_length=10, blank=True)
    assess_time = models.DateField(blank=True,null=True)


def __str__(self):
    return self.name


class Detail(models.Model):
    order = models.ForeignKey('Order', null=True, on_delete=models.SET_NULL, blank=True)
    supplier = models.CharField(max_length=10, blank=True)
    id = models.CharField(max_length=6, primary_key=True)
    applicant = models.CharField(max_length=10, blank=True)
    department = models.CharField(max_length=4, blank=True)
    send_time = models.DateField(blank=True)
    material_id = models.CharField(max_length=6)
    material_name = models.CharField(max_length=10, blank=True)
    specifications = models.CharField(max_length=10, blank=True)
    amount = models.IntegerField(blank=True)
    required_time = models.DateField(max_length=10, blank=True)
    state = models.CharField(max_length=3, default='未处理')
    remarks = models.CharField(max_length=100, blank=True)
    price = models.FloatField(blank=True,null=True)
    tran_price = models.FloatField(blank=True,null=True)
    rate = models.FloatField(blank=True,null=True)


def __str__(self):
    return self.name


