from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Employee
# Create your views here.

def fetchData(request):
    context = {}

    if  request.method =='POST':
        eno = int(request.POST['emp_no'])
        cur = connection.cursor()
        cur.execute('select * from emp where emp_no=%s',(eno,))
        data = cur.fetchall()
        print(data)
        #return HttpResponse('I am DBOperations')
        context['empinfo'] = data
        return render(request,'fetchdata.html',context)
    return render(request,'fetchdata.html')



def insertData(request):
    if request.method == "POST":
        eno = request.POST['emp_no']
        ename = request.POST['emp_name']
        esal = request.POST['emp_salary']
        eadd = request.POST['emp_address']
        edept = request.POST['dept_no']

        cur = connection.cursor()

        cur.execute('insert into emp values(%s,%s,%s,%s,%s)',
                    (eno,ename,esal,eadd,edept))
                    # (eno,ename,esal))
    return render(request,'insertData.html')
    
def ormInsertData(request):
    if request.method == "POST":
        ename = request.POST['empname']
        esal = request.POST['empsal']
        eadd = request.POST['empadd']

        emp = Employee(empname = ename,salary = esal,address = eadd)
        emp.save()

        return HttpResponse('Data saved Successfully')

    return render(request,'ormtemp.html')



def ormFetchData(request):

    data  = Employee.objects.all()
    print(data)
    return HttpResponse('Data Retrived')

def homepage(request):
    return render(request,'home.html')

def formExp(request):
    if request.method == 'POST':
        


        return render(request,'formExp.html')