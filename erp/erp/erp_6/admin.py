from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(WMS)
class WMSAdmin(admin.ModelAdmin):
    list_display = ['WMS_id', 'location', 'goods_id', 'goods_name', 'norms', 'volume', 'employ', 'ratio', 'charger_id', 'charger_name', ]
    search_fields = ['WMS_id', 'location', 'goods_id', 'goods_name', 'charger_id', 'charger_name', ]
    ordering = ('location',)


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display=['goods_id', 'goods_name', 'norms', 'WMS_id', 'location', 'amount_app', 'amount', 'unit', 'date_in', 'time', 'date_line', 'charger_id', 'charger_name', 'deal', ]


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display=['goods_id', 'goods_name', 'norms', 'characteristic', 'date', 'value', 'order_point', 'pur', 'state', 'stock_now', 'stock_real', 'stock_way', 'stock_secure', 'stock_free', 'unit', 'charger_id', 'charger_name', 'button', ]


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ['app_id', 'io', 'goods_id', 'goods_name', 'norms', 'demand', 'demand_io', 'unit', 'date_app', 'date_io', 'applicant', 'charger', 'charger', 'order', ]
    search_fields = ['goods_id', 'goods_name', 'app_id', 'date_app', 'applicant', 'charger', ]


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ['goods_id', 'goods_name', 'WMS_out_id', 'out_location', 'WMS_in_id', 'in_location', 'charger_out_id', 'charger_out_name', 'charger_in_id', 'charger_in_name', ]
    search_fields = ['goods_id', 'goods_name', 'WMS_out_id', 'out_location', 'WMS_in_id', 'in_location', 'charger_out_id', 'charger_out_name', 'charger_in_id', 'charger_in_name', ]


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ['app_id', 'WMS_id', 'location', ]
    search_fields = ['app_id', 'WMS_id', 'location', ]





