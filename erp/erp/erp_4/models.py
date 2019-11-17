from django.db import models
from erp_1.models import Staff, Department,Materials
# Create your models here.
class jianyandan(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    wuliaobianhao = models.ForeignKey('erp_1.Materials', null=True, on_delete=models.SET_NULL)

    jiagongzongxin_id = models.ForeignKey('erp_4.jiagongzhongxin', null=True, on_delete=models.SET_NULL)
    jyrid = models.ForeignKey('erp_1.Staff', null=True, on_delete=models.SET_NULL)

    chejianid = models.CharField(max_length=2,blank = True)
    shijian = models.DateField(blank = True)
    shuliang = models.CharField(max_length=10,blank = True)
    jieguo = models.BooleanField(default=True)

class paigongdan(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    jiagongzhongxin_id = models.ForeignKey('erp_4.jiagongzhongxin', null=True, on_delete=models.SET_NULL)
    wuliaobianhao = models.ForeignKey('erp_1.Materials', null=True, on_delete=models.SET_NULL)
    pgid = models.ForeignKey('erp_1.Staff', null=True, on_delete=models.SET_NULL)

    shijian = models.DateField(blank = True)


class zhizaodingdan(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    huohao = models.ForeignKey('erp_1.Materials', null=True, on_delete=models.SET_NULL)
    piliang = models.CharField(max_length=6,blank = True)
    chejianbianhao = models.CharField(max_length=6,blank = True)
    shijian = models.DateField(blank = True)
class jiagongzhongxin(models.Model):
    id = models.CharField(max_length=6,primary_key=True)
    xinghao = models.CharField(max_length=6,blank = True)
    chejianbianhao = models.CharField(max_length=6,blank = True)
    fuzeren = models.ForeignKey('erp_1.Staff', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id

