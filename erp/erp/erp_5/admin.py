from django.contrib import admin
from .models import*

# Register your models here.



@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'number', 'mail','address')
    search_fields = ('id',)



# admin.site.register(Supplier)
admin.site.register(Supply)
admin.site.register(Order)
admin.site.register(Detail)

