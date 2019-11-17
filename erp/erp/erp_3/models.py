from django.db import models


# MPS表单
class Mps_list(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    name = models.CharField(max_length=10,blank=True)
    start_time = models.DateField(blank=False)
    end_time = models.DateField(blank=False)


class Product_list(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    product_id = models.CharField(max_length=6)
    name = models.CharField(max_length=10,blank=True)
    forMps = models.ForeignKey(Mps_list,on_delete=models.CASCADE)


class TimeForProduct_list(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    time = models.DateField(blank=False)
    amount = models.IntegerField(blank=False)
    forProduct = models.ForeignKey(Product_list,on_delete=models.CASCADE)


# 输出表单   
class Purchase_apply(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    product_id = models.CharField(max_length=6)
    name = models.CharField(max_length=10,blank=True)
    standard = models.CharField(max_length=10,blank=True)
    apply_department = models.CharField(max_length=4,blank=False, default="MRP")
    for_mps = models.ForeignKey(Mps_list, on_delete=models.CASCADE)


class TimeForPurchase_list(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    time = models.DateField(blank=False)
    amount = models.IntegerField(blank=False)
    forProduct = models.ForeignKey(Purchase_apply,on_delete=models.CASCADE)


class Manufacture_apply(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    product_id = models.CharField(max_length=6)
    name = models.CharField(max_length=10,blank=True)
    applicant_id = models.CharField(max_length=6,blank=True)
    applicant_name = models.CharField(max_length=10,blank=True)
    for_mps = models.ForeignKey(Mps_list, on_delete=models.CASCADE)


class TimeForManufacture_list(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    in_time = models.DateField(blank=False)
    in_amount = models.IntegerField(blank=False)
    out_time = models.DateField(blank=False)
    out_amount = models.IntegerField(blank=False)
    forProduct = models.ForeignKey(Manufacture_apply,on_delete=models.CASCADE)
