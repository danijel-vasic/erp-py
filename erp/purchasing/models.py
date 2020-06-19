from django.db import models
from bom.models import Part
from sale.models import Sale;

# Buying stuff
  
class Buy(models.Model) :
  title = models.CharField(max_length=80)
  notes = models.TextField(blank=True)
  vender = models.CharField(max_length=80)
  sale = models.OneToOneField(Sale)  
  cost = models.DecimalField(max_digits=8,decimal_places=2)
  shippingCost = models.DecimalField("shipping Cost",max_digits=8,decimal_places=2)
  trackingNumber = models.TextField("tracking Number",blank=True)
  orderDate = models.DateField("order Date",auto_now_add=True)
  deliveryDate = models.DateField("delivery Date",null=True,blank=True)
  
  typeChoices = (
    ('open', 'Open'),
    ('delivered', 'Delivered'),    
    ('discarded', 'Discarded'),        
  )
  type = models.CharField(max_length=20,choices=typeChoices,default='open')

  def __str__(self):     
    return self.title   

class BuyPart(models.Model) :
  part = models.OneToOneField(Part)
  buy = models.OneToOneField(Buy)
  quantity = models.IntegerField()

class BuyRequest(models.Model) :
  sale = models.OneToOneField(Sale)  
  title = models.CharField(max_length=80)
  notes = models.TextField(null=True,blank=True)
  openDate = models.DateTimeField(auto_now_add=True)
  closeDate = models.DateTimeField(null=True,blank=True)

  typeChoices = (
    ('requested', 'Requested'),
    ('rfq', 'RFQ'),    
    ('close', 'Completed'),        
    ('canceled', 'Canceled'),        
  )
       
  type = models.CharField(max_length=25,choices=typeChoices,default='requested')

class RequestForQuoteBuy(models.Model) :
  buyRequest = models.OneToOneField(BuyRequest)
  part = models.OneToOneField(Part)
  quantity = models.IntegerField()

# Finance Dashbord, table
#   roll up total part and shipping costs for each sale
#   roll up total hours, labor costs, NRE costs per sale
#   roll up discarded buys per sale
#   compare to budget cost per sale
#   schedule
#
# List all child part numbers per sale
#   show all parts
#   show only parts with no buy request
#   show only ordered and undelivered buys
#   show open buy requests
# 
# Buy Requests
#   open, include 0 to N parts
#   convert into buy and close
#   cancel
#   mark as out for RFQ
#   export open requests as atom feed

# Buys
#   create directly without Buy Request
#   create from Buy Request
#   delete
#   mark as delivered
#   update price/shipping costs
#   update part list
#   export open buys as atom feed



