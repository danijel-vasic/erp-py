from django.db import models
from bom.models import Part
import datetime
from django.utils import timezone

# Sales

class Sale(models.Model):
  name = models.CharField(max_length=100)
  customer = models.CharField(max_length=100)  
  startDate = models.DateField(auto_now_add=True)
  scheduledShipDate = models.DateField("scheduled Ship Date")
  scheduledInvoiceDate = models.DateField("scheduled Invoice Date")   
  actualInvoiceDate = models.DateField("actual Invoice Date",null=True,blank=True)
  actualShipeDate = models.DateField("actual Ship Date",null=True,blank=True)  
  budgetDollars = models.IntegerField("Budget")
  notes = models.TextField(null=True,blank=True)
  
  # budget functions
  def bomCost(self):
    return 0
    
  def productionLaborCost(self):
    return 0
    
  def NRELaborCost(self):
    return 0
    
  def totalCost(self):
    return self.bomCost() + self.productionLaborCost() + self.NRELaborCost()
    
  def percentOfBudgetUsed(self):
    return "{:.1f}".format( self.totalCost() / self.budgetDollars * 100.0 )
    
  # status functions.
  def percentOfBOMReleased(self):
    return 0
    
  def percentOfBOMPurchased(self):
    return 0
    
  def percentOfBOMDelivered(self):
    return 0
    
  # schedule functions.  
  def daysUntilShip(self): 
    daysLeft = self.scheduledShipDate - timezone.now().date()
    return str(daysLeft.days)
             
  def __str__(self):     
    return self.name 

class SaleBOMEntry(models.Model) :
  parentPart = models.OneToOneField(Part)
  sale = models.OneToOneField(Sale)  
  quantity = models.IntegerField()

