from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def fb(request):
    email=request.GET['email1']
    password=request.GET['pass']
    return HttpResponse(f'welcome:{email}')


def fun(request):
    return render(request,'evenandodd.html')


def even_fun(request):
    number=int(request.GET['number'])
    e=''
    if number%2==0:
        e+='even'
    else:
        e+='odd'
    return HttpResponse(f'this number is {e}')