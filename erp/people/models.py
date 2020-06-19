from django.db import models
from sale.models import Sale

class People(models.Model):
  firstName = models.CharField('first Name',max_length=100)
  lastName = models.CharField('last Name',max_length=100)
  
  relationshipChoices = (
    ('employee', 'employee'),
    ('contractor','contractor'),
    ('none', 'none'),    
  )
     
  relationship = models.CharField(max_length=25,choices=relationshipChoices,default='employee')
  
  loadedHourlyCost = models.DecimalField('hourly Cost',max_digits=8,decimal_places=2)
  
  email = models.EmailField()

  def __str__(self):
    return self.firstName + ' ' + self.lastName

class TimeCardEntry(models.Model):
  employee = models.ForeignKey(People)
  sale = models.ForeignKey(Sale,null=True,blank=True)
  hours = models.DecimalField(max_digits=3,decimal_places=1)
  day = models.DateField()
  costDollars = models.DecimalField("cost",max_digits=8,decimal_places=2)
  
  typeChoices = (
    ('Production', 'Production'),
    ('NRE', 'NRE'),
    ('Other', 'Other'),    
  )
     
  type = models.CharField(max_length=25,choices=typeChoices)
  
  paidFor = models.BooleanField(default=False)
  
  enterDate = models.DateTimeField("enter Date",auto_now_add=True)
  enterUser = models.CharField(max_length=100,null=True,blank=True)
  
  note = models.CharField(max_length=100)