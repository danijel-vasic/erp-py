from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'erp.views.home', name='home'),
  url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'erp/login.html'}),  
  url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{ 'next_page':'/'} ),  
  url(r'^bom/', include('bom.urls')),
  url(r'^people/', include('people.urls')),
  url(r'^vendor/', include('vendors.urls')),
  url(r'^purchasing/', include('purchasing.urls')),    
  url(r'^sale/', include('sale.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
