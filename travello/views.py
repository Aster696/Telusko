from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'Mumbai - 400099'
    dest1.price = '777'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Goa'
    dest2.desc = 'Goa - 400869'
    dest2.price = '1000'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Dheli'
    dest3.desc = 'Dheli - 603099'
    dest3.price = '500'
    dest3.offer = False
    
    data = [dest1, dest2, dest3]
    return render(request, 'travello.html', {"list": data})