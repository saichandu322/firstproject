from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'chandu': 'superman'})

def personal(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length',12))
    choise=['1','2','3','4','56','a','s','d','f','g']
    if request.GET.get('UpperCase'):
        choise.extend(list('ABCDEFGHIJKLMNOPQRSTVUWXYZ'))
    randpass=''
    for i in range(length):
        randpass+=random.choice(choise)

    return render(request, 'generator/password.html',{'password':(randpass)})
def about(request):
    return render(request, 'generator/about.html')

def login(request):
    return render(request, 'generator/login.html')

def fuckyou(request):
    username=request.GET.get('username')
    passw=request.GET.get('password')
    return render(request, 'generator/fuckyou.html',{"Username":username,"Password":passw})