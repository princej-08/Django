from django.shortcuts import render,redirect
from django.http import HttpResponse
# from DBOperations.models import Employee
from django.db.models import Count, Min, Max, Sum
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View


from .forms import EmpForm,CustUserCreate,ImageExp
from .models import Employee,Product

# Create your views here.
@login_required(login_url='login')
def ormExample(request):

    # data = Employee.objects.all()
    # data = Employee.objects.filter(empname__startswith = 'P')
    # data = Employee.objects.filter(salary__gt =100000)
    # print(data)

    # for rec in data:
    #     print(rec.empname,rec.salary)
    # cnt = Employee.objects.aggregate(Count('empname'))
    # print(cnt)
    # data = Employee.objects.all().order_by('empname')
    # data = Employee.objects.values('dept_no').annotate(Sum('salary'))
    # print(data)
    # return HttpResponse('I am revision app')
    context = {}
    obj = EmpForm()
    context['empform'] = obj

    if request.method == "POST":
        data = EmpForm(request.POST)

        if data.is_valid():
            # eno = data.cleaned_data['empno']
            # ename = data.cleaned_data['empname']
            # esalary = data.cleaned_data['salary']

            # empobj = Employee(empno = eno,empname = ename, salary = esalary)
            # empobj.save() 
            data.save()
            return HttpResponse('Data Saved Successfully')
        else:
            print(data.errors)
            return HttpResponse('Failed to Save')
    return render(request, 'revision.html',context)

def userLogin(request):
    context = {}

    if request.method == "POST":
        uname = request.POST['uname']
        upwd = request.POST['password']

        validUser = authenticate(username=uname, password=upwd)

        if validUser is not None:
            obj = EmpForm()
            context['empform'] = obj
            print(request.user.is_staff)
            if request.user.is_authenticated:
                return render(request, 'revision.html', context)
            else:
                login(request, validUser)
                messages.add_message(
                    request, level=messages.INFO, message='successfully logged in')
                return render(request, 'revision.html', context)
        else:
            return HttpResponse('You are not valid user')

    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return render(request,'login.html')


def createUser(request):
    context = {}
    obj = CustUserCreate
    context['signupform'] = obj

    if request.method == "POST":
        newUser = CustUserCreate(request.POST)
        if newUser.is_valid():
            newUser.save()
            messages.success(request, 'User Successfully Created')
            return redirect('login')
        else:
            print(newUser.errors)
            messages.error(request, 'Having Some Errors')
            return redirect('signup')


    return render(request,'signup.html',context)

@user_passes_test(lambda user: user.is_staff,login_url='login')
def impFunction(request):
    return HttpResponse('I am Important Function')


def imageProcessing(request):
    context = {}
    context['form'] = ImageExp()

    if request.method == "POST":
        data = ImageExp(request.POST,request.FILES)

        if data.is_valid():
            data.save()
            return HttpResponse('Data Saved Successfully')
        else:
            print(data.errors)
            return HttpResponse("Data is not Saved")

    return render(request,'image.html',context)


def homepage2(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    return render(request,'home2.html',context)


def dynamicURL(request,value):

    # return HttpResponse(f'I have got {value} value')
    context = {}
    info = Product.objects.filter(prdId=value)
    context['info'] = info
    return render(request,'prodInfo.html',context)



class MyView(View):
    def get(self,request):
        # return HttpResponse('I am My View')
        return render(request,'classExp.html')

    def post(self,request):
        return HttpResponse(f"I have received {request.POST['name1']}")

