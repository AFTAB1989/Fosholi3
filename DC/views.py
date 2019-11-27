from django.http import HttpResponse
from django.shortcuts import render
from DC.forms import registerForm


def show(request):
    return render(request, 'DChome.html')


def login_pg(request):
    return render(request, 'upcReg.html')

def register(request):
    form = registerForm() 

    if request.method == "POST":
        form = registerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return show(request)
        else:
            print('Invalid form')

    return render(request, 'registerChairman.html',{'form':form})
