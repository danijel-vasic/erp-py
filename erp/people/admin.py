from django.contrib import admin
from people.models import *;

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName','relationship','loadedHourlyCost')

admin.site.register(People,PeopleAdmin)

class TimeCardEntryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'day','hours','costDollars','sale')

admin.site.register(TimeCardEntry,TimeCardEntryAdmin)

