from django.contrib import admin
from purchasing.models import *;

class BuyAdmin(admin.ModelAdmin):
    list_display = ('type','orderDate','deliveryDate','title', 'vender','cost','shippingCost','trackingNumber')

admin.site.register(Buy,BuyAdmin)
admin.site.register(BuyPart)
admin.site.register(BuyRequest)
admin.site.register(RequestForQuoteBuy)