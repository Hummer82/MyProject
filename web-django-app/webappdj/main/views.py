from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.

def index(request):
    #return HttpResponse("<h4>Проверка работы</4>")
    return render(request,"main/index.html")

def about(request):
    #return HttpResponse("<h4>Про нас</4>")
    return render(request,"main/about.html")