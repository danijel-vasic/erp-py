from django.contrib import admin
from bom.models import *;

# Register your models here.

class PartAdmin(admin.ModelAdmin):
    list_display = ('partName', 'revision','description','type')

admin.site.register(Part,PartAdmin)

admin.site.register(assemblyPart)
admin.site.register(partVendor)
admin.site.register(partFabricationRequiredCapabilities)