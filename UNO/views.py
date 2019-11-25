from django.http import HttpResponse
from django.shortcuts import render


def show(request):
    return HttpResponse("<h1>UNO Home Page</h1>")

