from django.contrib import admin
from sale.models import *;

class SaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer','scheduledShipDate')
admin.site.register(Sale,SaleAdmin)
admin.site.register(SaleBOMEntry)

# Register your models here.
