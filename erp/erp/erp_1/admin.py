from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'manager', 'info',)
    search_fields = ('id',)


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'specification', 'Quota', 'safety_stock_quantity', 'item', 'is_buy',)
    list_filter = ('type',)
    search_fields = ('name', 'info',)
    ordering = ('id',)
    fields = ('id', 'name', 'type', 'specification', 'Quota', 'safety_stock_quantity', 'item', 'is_buy',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'department', 'on_the_job', 'phone_number', 'mail',)


@admin.register(ProductionProcess)
class ProductionProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'leading_man', 'required_time')
    search_fields = ('id',)


@admin.register(Bom)
class BomAdmin(admin.ModelAdmin):
    list_display = ('id', 'materials', 'parent_code', 'leadtime', 'consumption', 'bom_level')
    search_fields = ('id',)


@admin.register(FlowOfProduction)
class FlowOfProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'leading_man', 'required_time',)
    search_fields = ('id',)


@admin.register(ProductionChain)
class ProductionChainAdmin(admin.ModelAdmin):
    list_display = ('pre', 'process', 'next',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
