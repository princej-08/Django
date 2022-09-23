from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def evennumber(request):
   if request.method == 'POST':
      
   
      return HttpResponse('Hello Django')
   # return render(request,'application.html')
        
  