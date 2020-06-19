from django.conf.urls import patterns, url

from people import views

urlpatterns = patterns('',
  url(r'^addtimecard$', views.addtimecard, name='addtimecard'),
  url(r'^(?P<peopleid>\d+)/addtimecard$', views.addtimecardid, name='addtimecardid'),
)