from django.db import models

# Create your models here.

class Department(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=20)

    def __str__(self):
        return self.deptname

        
class Employee(models.Model):
    empname = models.CharField(max_length = 20)
    salary = models.IntegerField()
    address = models.TextField(max_length =200,null=True)
    dept_no = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    

    def __str__(self):
        return self.empname

    class Meta:
        ordering =['-empname']
        


        