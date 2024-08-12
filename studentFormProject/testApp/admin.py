from django.contrib import admin
from testApp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):

    list_display=["name","department","marks"]

admin.site.register(Student,StudentAdmin)


