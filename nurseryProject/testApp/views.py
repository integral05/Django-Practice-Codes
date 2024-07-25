from django.shortcuts import render
import datetime
# Create your views here.

def  dateinfo(request):
    date = datetime.datetime.now()
    name = "Integral"
    
    msg=""
    h = int(date.strftime('%H'))
    if h < 12:
        msg= "Good Morning!!!"
    elif h < 17:
        msg= "Good Afternoon!!!"
    elif h < 22:
        msg = "Good Evening!!!"
    else:
        msg = "GoodNight!!!"


    my_dict = {'date' : date,'name': name,'wish' : msg}

    return render(request,'testApp/test.html',context=my_dict)
