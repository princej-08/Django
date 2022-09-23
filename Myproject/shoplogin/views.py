from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def shopLogin(request):
    context={}

    if request.method == 'POST':
        uname = request.POST['uname']
        upwd = request.POST['pwd']

        validUser = authenticate(username=uname, password=upwd)
        
        if validUser is not None:
            print(request.is_staff) 
            if request.user.is_authenticated:
                return render(request,'shoplogin.html',context)
            else:
                login(request, validUser)
                return render(request,'shoplogin.html',context) 
        else:
            return HttpResponse('You are not valid User')

    return render(request,'shoplogin.html')
