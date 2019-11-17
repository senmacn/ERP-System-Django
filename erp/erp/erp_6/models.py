from django.db import models


# Create your models here.


class WMS(models.Model):
    WMS_id = models.CharField(max_length=2, blank=True)
    location = models.CharField(max_length=10, primary_key=True)
    goods_id = models.CharField(max_length=6, blank=True)
    goods_name = models.CharField(max_length=10, blank=True)
    norms = models.CharField(max_length=10, blank=True)
    volume = models.IntegerField(default=10000)
    employ = models.IntegerField(default=0)
    ratio = models.FloatField(default=0)
    charger_id = models.CharField(max_length=6, blank=True)
    charger_name = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.WMS_id


class Goods(models.Model):
    # Goodsapp = models.ForeignKey('App', null=True, on_delete=models.SET_NULL)
    # Goodschange = models.ForeignKey('Change', null=True, on_delete=models.SET_NULL)
    id = models.CharField(max_length=6, default=000000, primary_key=True)
    goods_id = models.CharField(max_length=6, blank=True)
    goods_name = models.CharField(max_length=10, blank=True)
    norms = models.CharField(max_length=10, blank=True)
    WMS_id = models.CharField(max_length=2, blank=True)
    location = models.CharField(max_length=10, blank=True)
    # ined = models.BooleanField(default=0)
    amount_app = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    unit = models.CharField(max_length=5, blank=True)
    date_in = models.DateField(blank=True)
    time = models.CharField(max_length=5, blank=True)
    date_line = models.DateField(blank=True)
    charger_id = models.CharField(max_length=6, blank=True)
    charger_name = models.CharField(max_length=10, blank=True)
    deal = models.IntegerField(default=0)

    def __str__(self):
        return self.goods_id


class Check(models.Model):
    id = models.CharField(max_length=14, default=00000000000000, primary_key=True)
    # goods = models.ForeignKey('Materials', null=True, on_delete=models.SET_NULL)
    goods_id = models.CharField(max_length=6, blank=True)
    goods_name = models.CharField(max_length=10, blank=True)
    norms = models.CharField(max_length=10, blank=True)
    characteristic = models.CharField(max_length=10, blank=True)
    value = models.CharField(max_length=1, blank=True)
    order_point = models.CharField(max_length=6, blank=True)
    date = models.DateField(blank=True, auto_now=True)
    pur = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=6, blank=True)
    stock_now = models.IntegerField()
    stock_way = models.IntegerField()
    stock_secure = models.IntegerField()
    stock_real = models.IntegerField()
    stock_free = models.IntegerField()
    unit = models.CharField(max_length=5, blank=True)
    charger_id = models.CharField(max_length=6, blank=True)
    charger_name = models.CharField(max_length=10, blank=True)
    button = models.CharField(max_length=10, default='补货申请')

    def __str__(self):
        return self.goods_id


class App(models.Model):
    app_id = models.CharField(max_length=6, primary_key=True)
    io = models.CharField(max_length=1, blank=True)
    goods_id = models.CharField(max_length=6, blank=True)
    goods_name = models.CharField(max_length=10, blank=True)
    norms = models.CharField(max_length=10, blank=True)
    demand = models.IntegerField(blank=True)
    demand_io = models.IntegerField(default=0, blank=True)
    unit = models.CharField(max_length=5, blank=True)
    date_app = models.DateField()
    date_io = models.DateField(blank=True)
    applicant = models.ForeignKey('erp_1.Staff', verbose_name='申请人',related_name='applicant', null=True, on_delete=models.SET_NULL)
    # applicant_id = models.CharField(max_length=6, blank=True)
    # applicant_name = models.CharField(max_length=10, blank=True)
    # applicant_tel = models.CharField(max_length=20, blank=True)
    # applicant_depart = models.CharField(max_length=4, blank=True)
    charger = models.ForeignKey('erp_1.Staff', verbose_name='管理员',related_name='charger', null=True, blank=True, on_delete=models.SET_NULL)
    # charger_id = models.CharField(max_length=6, blank=True)
    # charger_name = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=6, blank=True)
    order = models.ForeignKey('erp_5.Order', null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.app_id


class Move(models.Model):
    goods_id = models.CharField(max_length=6, primary_key=True)
    goods_name = models.CharField(max_length=10, blank=True)
    WMS_out_id = models.CharField(max_length=2, blank=True)
    out_location = models.CharField(max_length=10, blank=True)
    WMS_in_id = models.CharField(max_length=2, blank=True)
    in_location = models.CharField(max_length=10, blank=True)
    charger_out_id = models.CharField(max_length=6, blank=True)
    charger_out_name = models.CharField(max_length=10, blank=True)
    charger_in_id = models.CharField(max_length=6, blank=True)
    charger_in_name = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.goods_id


class Change(models.Model):
    # apped = models.ForeignKey('App', null=True, on_delete=models.SET_NULL)
    app_id = models.CharField(max_length=6, primary_key=True)
    WMS_id = models.CharField(max_length=2, blank=True)
    location = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.app_id