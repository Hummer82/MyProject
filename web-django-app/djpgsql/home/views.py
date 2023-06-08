from django.shortcuts import render

def home(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request,"home/index.html",data)
