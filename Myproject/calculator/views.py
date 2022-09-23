from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.

def addition(request):
    context = {}
    if request.method == 'POST':
        # print(request.POST)
        a = int(request.POST['num1'])
        b = int(request.POST['num2'])

        if 'add' in request.POST:
            c = a+b
            context['value'] = c
        elif 'sub' in request.POST:
            c = a-b
            context['value'] = c
        elif 'div' in request.POST:
            c = a//b
            context['value'] = c
        elif 'mul' in request.POST:
            c = a*b
            context['value'] = c

        # context['name'] = 'calculator'
        # context['listvalues'] = [10,12,14,16]
        return render(request, 'addition.html', context)
        # return HttpResponse ('Addition is : ' +str(c))
    return render(request, 'addition.html')
    

# def addition1(request):
#     if request.method == 'POST':
#         # print(request.POST)
#         a = int(request.POST['num1'])
#         b = int(request.POST['num2'])
#         c = a+b

#         return HttpResponse ('Addition is : ' +str(c))
#     return render(request, 'addition.html')