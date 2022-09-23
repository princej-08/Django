from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def firstFun(request):
    # return HttpResponse("Hi I'M First Function")
    context = {'name': 'Raju','age': 34}
    return render(request,'welcome.html',context)

def secondFun(request):
    return render(request, 'Details.html')

def thirdFun(request):
    print('I am Third function')
    # print(request.GET)
    print(request.POST)
    return HttpResponse('Hello Python')