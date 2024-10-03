from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,"testapp/name.html")

def age_view(request):
    name = request.GET['name']
    resopnse =  render(request,"testapp/age.html")
    resopnse.set_cookie('name',name)

    return resopnse

def gf_view(request):
    age = request.GET['age']
    resopnse =  render(request,"testapp/girlfriend.html")
    resopnse.set_cookie('age',age)

    return resopnse

def results_view(request):
    gfname=request.GET['gfname']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    response = render(request,"testapp/results.html",{'user_name':name,'user_age':age,'user_gfname':gfname})

    return response

