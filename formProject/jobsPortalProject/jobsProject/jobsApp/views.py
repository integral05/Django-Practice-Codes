from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsinfo(request):
    s="<h1>Jobs available in Hyderabad</h1>"
    return HttpResponse(s)

def punejobsinfo(request):
    s="<h1>Jobs available in Pune</h1>"
    
    return HttpResponse(s)

def mumbaijobsinfo(request):
    s="<h1>Jobs available in Mumbai</h1>"
    return HttpResponse(s)

def chennaijobsinfo(request):
    s="<h1>Jobs available in Chennai</h1>"
    return HttpResponse(s)