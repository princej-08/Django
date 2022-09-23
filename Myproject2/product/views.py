from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    # return HttpResponse('My Product')

    return render(request,'base.html')

def mobiles(request):
    return render(request, 'mobiles.html')

def furnitures(request):
    return render(request, 'furnitures.html')

def personalcare(request):
    return render(request, 'personalcare.html')

def toys(request):
    return render(request, 'toys.html')

def grocery(request):
    return render(request, 'grocery.html')

def electronics(request):
    return render(request, 'electronics.html')

def fashion(request):
    return render(request, 'fashion.html')
