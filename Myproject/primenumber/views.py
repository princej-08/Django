from re import S
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def primenumber(request):
    context = {}
    if request.method == 'POST':
        value = int(request.POST['num'])
        for i in range(2,value+1):
            if value % i == 0:
                if i == value:
                    s = 'Prime'
                    context['value'] = s
                    break
                else:
                    d = 'Not a Prime'
                    context['value'] = d
                    break

        return render(request,'primenumber.html',context)
    return render(request,'primenumber.html')