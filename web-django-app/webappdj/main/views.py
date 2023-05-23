from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.

def index(request):
    data = {
        'title':'Главная страница',
        'values': ['Some','Hello'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    #return HttpResponse("<h4>Проверка работы</4>")
    return render(request,"main/index.html",data)

def about(request):
    #return HttpResponse("<h4>Про нас</4>")
    return render(request,"main/about.html")

def contacts(request):
    #return HttpResponse("<h4>Про нас</4>")
    return render(request,"main/contacts.html")