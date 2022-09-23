from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def table(request):
    mtable = []
    context = {}
    if request.method == 'POST':
        val = int(request.POST['num'])
        for i in range(1,11):
            s =str(val) + ' * ' + str(i) + ' = ' + str(i * val)
            mtable.append(s)
            context['output'] = mtable 

        return render(request,'mathtable.html',context)
    return render(request,'mathtable.html')
