from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    userlist = [
        {'name': 'Dima'},
        {'name': 'Vova'},
        {'name': 'Kolya'},
    ]
    cntx = {'name': 'Dima', 'userlist': userlist}

    return render(request,'index.html',cntx)