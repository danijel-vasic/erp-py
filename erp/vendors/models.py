from django.db import models

# sheet metal, machine shop, water cutting, grinding, black oxide,
# paper targets, plastic targets, scale bar certification
class VendorCapabilityType(models.Model):
  name = models.CharField(max_length=100)
  notes = models.TextField(null=True,blank=True)
  
# the name of a vender
class Vendor(models.Model):
  name = models.CharField(max_length=100)
  website = models.CharField("URL",max_length=512)
  onlineAccountName = models.CharField("online Account Name",max_length=512)
  notes = models.TextField(null=True,blank=True)
  
class VendorContact(models.Model):
  vender = models.OneToOneField(Vendor)  
  contactName = models.CharField(max_length=512)
  contactEmail = models.CharField(max_length=512)
  contactPhone = models.CharField(max_length=512)
  notes = models.TextField(null=True,blank=True)

# what if any fabrication capabilities the vender has 
class VendorCapabilities(models.Model):
  vender = models.OneToOneField(Vendor)
  type   = models.OneToOneField(VendorCapabilityType)
  notes = models.TextField(null=True,blank=True)

  typeChoices = (
    ('primary', 'Primary'),
    ('sub', 'Subcontract'),    
  )
       
  type = models.CharField(max_length=25,choices=typeChoices)
 
 
# No non-admin user pages for vendors, created as needed in BOM/buy area.

