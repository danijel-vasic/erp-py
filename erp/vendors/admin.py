from django.contrib import admin
from vendors.models import *;

# Register your models here.

admin.site.register(VendorCapabilityType)
admin.site.register(Vendor)
admin.site.register(VendorContact)
admin.site.register(VendorCapabilities)