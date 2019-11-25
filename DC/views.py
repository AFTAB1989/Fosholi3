from django.http import HttpResponse
from django.shortcuts import render


def show(request):
    return render(request, 'DChome.html')


def login_pg(request):
    return render(request, 'upcReg.html')
