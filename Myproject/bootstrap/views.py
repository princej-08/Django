from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bootstrapExp(request):
    return HttpResponse('I am Bootstrap')