from django.shortcuts import render
from .import forms
# Create your views here.

def studentRegisterView(request):
    form = forms.StudentRegistration()

    return render(request,'testApp/register.html',{'form':form})


