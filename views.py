from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.urls import reverse
import datetime
from .forms import CreateTeacher

def index(request):
    #list = get_object_or_404 ()      
    if request.method == 'POST':
        form = CreateTeacher(request.POST)
        print (request.POST.get('FirstName'))
        print (request.POST.get('LastName'))
        
        print (form['firstname'].value())
        print (form.data['FirstName'])
        
        if form.is_valid():
            
            print (form.cleaned_data['FirstName'])
            print (form.instance.FirstName)
            
            form.save()
            print (form.instance.id)
    #list.save()         
        
        
        
    return render_to_response('databasepage.html')
