from django.shortcuts import render
from http import HttpResponse
from datetime 
from template import index
# Create your views here.


#def newyear(request):
 #   return HttpResponse("Hello World!")


def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear\templates\newyear\index.html", {
        "newyear": now.month == 1 and now.day == 1 




    }  )
