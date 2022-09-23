from django.contrib import admin
from .models import Employee, Department


# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['empname','salary','address','salaryType']
    list_filter = ['address','salary']

    def salaryType(self,obj):

        if obj.salary>150000:
            return 'High'
        else:
            return 'Low'




admin.site.register(Employee,EmpAdmin)
admin.site.register(Department)

