
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from Myproject.DBOperations.models import Employee
from .models import Employee, Product

# class EmpForm(forms.Form):
#     empno = forms.IntegerField()
#     empname = forms.CharField(max_length=10)
#     salary = forms.IntegerField()

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = "__all__"
        fields = ['empno','empname','salary']

class CustUserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','is_staff','email']

class ImageExp(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"