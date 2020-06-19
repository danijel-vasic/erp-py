from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from people.models import People, TimeCardEntry
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
 
@login_required
def addtimecard(request):

  if 'name' in request.GET:
    id = request.GET['name']
    return redirect( '/people/' + id + '/addtimecard' );      
  else:
    defaultPerson = People.objects.filter( firstName=request.user.first_name).filter(lastName=request.user.last_name)
  
    if (defaultPerson.count() == 1):
      return redirect( '/people/' + str(defaultPerson[0].id) + '/addtimecard' );
            
    people = People.objects.exclude( relationship='none') 
    if ( people.count() > 0 ):
      return redirect( '/people/' + str(people[0].id) + '/addtimecard' );
            
    class SelectPersonForm(forms.Form):
      firstName = forms.ModelChoiceField(people,empty_label=None)    
    filterForm = SelectPersonForm()

    return render(request, 'people/addtimecard.html', {'filterForm':filterForm})
    
@login_required
def addtimecardid(request,peopleid):

  people = People.objects.exclude( relationship='none') 
  currentPerson = people.filter( id=peopleid) 
  if ( currentPerson.count() != 1 ) :
    return HttpResponse('Invalid URL')

  class SelectPersonForm(forms.Form):
    name = forms.ModelChoiceField(people,empty_label=None,)
  filterForm = SelectPersonForm(initial = {'name': currentPerson[0].id })
  

  class SelectTimeEntry(forms.Form):
    date1 = forms.DateField()
    hours = forms.IntegerField()
    sale = forms.IntegerField()
    type = forms.IntegerField()
          
  timeEntryFormSet = formset_factory(SelectTimeEntry,extra=5)
  
  # find latest 5 cards for current user
  # enumerate every date from latst date to today, showing no more than 10 days
  # show date picker for each date
  # show hour field for each date
  # show choice field for work type.
  # show note field
  # show read only list of last N timecards.

  return render(request, 'people/addtimecard.html', {'filterForm':filterForm,'timeEntryFormSet':timeEntryFormSet})

