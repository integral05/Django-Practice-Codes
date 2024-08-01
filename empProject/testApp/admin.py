from django.contrib import admin
from testApp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['enum','ename','esal','eaddr',]




# Register your models here.
admin.site.register(Employee,EmployeeAdmin)


