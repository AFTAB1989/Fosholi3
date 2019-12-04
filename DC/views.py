from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from DC.forms import registerForm
from django.contrib import messages

# DC index page
from UpChairman.forms import RegisterForm


def show(request):
    return render(request, 'DChome.html')


# dc login page
def login_pg(request):
    return render(request, 'upcReg.html')


# dc chairman register page
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True) #saves from data in model
            messages.success(request, f'New account created successfully !')
            return redirect(register)
        else:
                messages.success(request, f'Could not create new acount. Something went wrong')
                return render(request, 'registerChairman.html',{'form':form})

    return render(request, 'registerChairman.html', {'form': form})
