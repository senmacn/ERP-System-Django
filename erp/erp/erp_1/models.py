from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=6, blank=True)
    user = models.ManyToManyField(User, related_name='user_role')


class Department(models.Model):
    # 部门信息
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=4)
    manager = models.CharField(max_length=10, blank=True)
    info = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Materials(models.Model):
    # 物料信息
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=2)
    specification = models.CharField(max_length=10)
    Quota = models.IntegerField(blank=True)
    safety_stock_quantity = models.IntegerField(blank=True)
    is_buy = models.BooleanField(blank=True, default=True)
    item = models.CharField(max_length=2, default='物料')

    def __str__(self):
        return self.name


class Staff(models.Model):
    # 员工信息
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL)
    on_the_job = models.BooleanField(blank=True)
    qualification = models.CharField(max_length=10, blank=True)
    native_place = models.CharField(max_length=20, blank=True)
    post = models.CharField(max_length=10, blank=True)
    level = models.CharField(max_length=5, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    nation = models.CharField(max_length=5, blank=True)
    seniority = models.IntegerField(blank=True) # 工龄
    mail = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class ProductionProcess(models.Model):
    # 生产工序
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=10)
    materials = models.ForeignKey('Materials', null=True, on_delete=models.SET_NULL)
    leading_man = models.ForeignKey('Staff', null=True, on_delete=models.SET_NULL)
    required_time = models.IntegerField()
    note = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class FlowOfProduction(models.Model):
    # 生产流程
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=10)
    leading_man = models.ForeignKey('Staff', null=True, on_delete=models.SET_NULL)
    required_time = models.IntegerField(default=10)
    productionChain = models.OneToOneField('ProductionChain', related_name='chain', null=True, on_delete=models.SET_NULL)

    note = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class ProductionChain(models.Model):
    pre = models.OneToOneField('ProductionChain', related_name='pre0', blank=True, null=True, on_delete=models.SET_NULL)
    process = models.ForeignKey('ProductionProcess', null=True, on_delete=models.SET_NULL)
    next = models.OneToOneField('ProductionChain', related_name='next0', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.process.name


class Bom(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    materials = models.ForeignKey('Materials', null=True, on_delete=models.SET_NULL)
    parent_code = models.CharField(max_length=6, blank=True)
    leadtime = models.IntegerField()
    consumption = models.IntegerField()
    bom_level = models.IntegerField()

    def __str__(self):
        return self.materials.name
