from django.shortcuts import render
from testApp.models import *

# Create your views here.

def index(request):

    return render(request,'testApp/index.html')


def puneJobs1(request):
    jobs_list = PuneJobs.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request,'testApp/punejobs.html',context=jobs_list)

def hydJobs1(request):

    return render(request,'testApp/hydjobs.html')

def bloreJobs1(request):

    return render(request,'testApp/blorejobs.html')

def chennaiJobs1(request):

    return render(request,'testApp/chennaijobs.html')

