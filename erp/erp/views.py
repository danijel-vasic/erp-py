from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from sale.models import Sale
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    sales_list = Sale.objects.all().order_by('-startDate')[:10]
    return render(request, 'erp/index.html', {'sales': sales_list})
    
