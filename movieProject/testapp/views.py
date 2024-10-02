from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm 

# Create your views here.
def index_view(request):

    return render(request,'testapp/index.html')






