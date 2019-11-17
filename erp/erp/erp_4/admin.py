from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(paigongdan)
class paigongdanAdmin(admin.ModelAdmin):
    list_display = ('id', 'jiagongzhongxin_id', 'wuliaobianhao', 'pgid','shijian',)
    search_fields = ('id',)


@admin.register(zhizaodingdan)
class zhizaodingdanAdmin(admin.ModelAdmin):
    list_display = ('id', 'huohao', 'piliang', 'chejianbianhao','shijian',)
    list_filter = ('huohao',)
    search_fields = ('piliang',)
    ordering = ('id',)
    fields = ('id', 'huohao', 'piliang', 'chejianbianhao','shijian',)

@admin.register(jianyandan)
class jianyandanAdmin(admin.ModelAdmin):
    list_display = ('id', 'wuliaobianhao', 'jiagongzongxin_id', 'jyrid',  'chejianid','shijian','shuliang',)

@admin.register(jiagongzhongxin)
class jiagongzhongxinAdmin(admin.ModelAdmin):
    list_display = ('id', 'xinghao', 'chejianbianhao', 'fuzeren',)


