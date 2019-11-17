from django.db import models

# Create your models here.


class Staff(models.Model):
    # 人员
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=10)
    zhiwu = models.CharField(max_length=10)
    yeji = models.FloatField(default=0)
    tel = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    # 客户
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    grade = models.FloatField(default=0)
    tel = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    # 产品
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=10)
    cost = models.IntegerField(default=0)
    basic_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order2(models.Model):
    # 订单
    id = models.CharField(max_length=6, primary_key=True)
    customer = models.ForeignKey('Customer', null=True, on_delete=models.SET_NULL)
    salesman = models.ForeignKey('erp_1.Staff', verbose_name='销售员',related_name='salesman', null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey('Product', null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    date = models.DateField()
    deliver2 = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.id


