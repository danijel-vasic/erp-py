from django.db import models
from vendors.models import Vendor

# BOM (bill of material) models

class Part(models.Model):
  partName = models.CharField(max_length=100)
  revision = models.IntegerField(default=0)
    
  creationDate = models.DateTimeField(auto_now_add=True)
  description = models.TextField(null=True,blank=True)
  notes = models.TextField(null=True,blank=True)
  
  typeChoices = (
    ('top', 'Top Level'),
    ('fastener', 'Fastener'),
    ('normal', 'Normal'),
  )
     
  type = models.CharField(max_length=25,choices=typeChoices,default='normal')
  
  def __str__(self):
    return self.partName + " R" + str(self.revision).zfill(2)

class assemblyPart(models.Model):
  childQuantity = models.IntegerField()
  parentPart = models.OneToOneField(Part,related_name='parent')
  childPart = models.OneToOneField(Part,related_name='child')
   

# a part can have 0 to N vendors, also the OEM is kept here.
# parts with no vendors or OEMs are made by TCM.
class partVendor(models.Model):
  parentPart = models.OneToOneField(Part,verbose_name="part Number")
  vendorPartName = models.CharField("vender Part Name",max_length=100)
  vendorName = models.CharField("Vender Name",max_length=100) 

  typeChoices = (
    ('manufacturer', 'Orginal Manufacturer'),
    ('reseller', 'Reseller'),    
  )
       
  type = models.CharField(max_length=25,choices=typeChoices,default='reseller')

# parts can have vender capabilities 
class partFabricationRequiredCapabilities(models.Model):
  parentPart = models.OneToOneField(Part,verbose_name="part Number")
  capability = models.CharField(max_length=100) 

# BOM operations.
  
# create a new part
#   prompt for manufacture name, manufacture part#
#   prompt for vender name, vender part#
# create a new part, and make it a child of an existing part. 
# create a new revision of an existing Part.
#   all of the dependent assemblyPart are copied and made to point to the new part ID. 
#   the latest revision of all parent assemblyParts are updated to use the new part ID
#   all of the dependent venders are copied
#   all of the dependent capabilities are copied.
# adding an assemblyPart reference to an existing part.
# deleting an assemblyPart reference (the default action of delete)
# deleting an Part
#   parts can only be deleted if they are a not dependent of an assemblyPart 
#   A deleted part deletes its dependent assemblyPart 
#   A deleted part does not delete Parts dependent Parts in assemblyPart rows
#   A deleted part deletes its dependent vendors
#   A deleted part deletes its dependent capabilities

# A part is orphaned if it is not topLevel and is not pointed to by any latest rev assemblyPart
# change part name
#  changes part name on all revisions.




