from asyncio import events
from operator import index
from django.shortcuts import redirect, render
from requests import request

from app.forms import RegistrationForm
from .models import Event
from django.http import FileResponse
import io
#from reportlab.pdfgen import canvas
#from reportlab.lib.units import inch
#from reportlab.lib.pagesizes import letter
from .models import Venue

# Generate Event  PDF
#

def home(request):
    
    home = Event.objects.filter(approval=True)
    return render(request, "home.html", {'home':home ,})

    
        
        


def index(request):   
    
    events = Event.objects.all()
    return render(request, "events.html", {'events':events})
    

def add_events(request):
      
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.save()
    else:
        form = RegistrationForm()
        
          
    print("form:",form)
    venue = Event.objects.all()
    return render(request, "add_events.html", {'venue':venue,'form':form })


    