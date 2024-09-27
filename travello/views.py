from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    data = Destination.objects.all()
    return render(request, 'travello.html', {"list": data})