from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'Mumbai - 400099'
    dest1.price = '777'
    return render(request, 'home.html', {'dest1': dest1})

def add(request): 
    result = int(request.POST["num1"]) + int(request.POST["num2"])
    return render(request, 'result.html', {'result': result})