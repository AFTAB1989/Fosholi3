from django.contrib import messages
from django.shortcuts import render, redirect

from UpChairman.forms import RegisterForm


def show(request):
    return render(request, 'upcHome.html')


def login_pg(request):
    return render(request, 'upcReg.html')


# UPC registering UNO page
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)  # saves from data in model
            messages.success(request, f'New UNO added successfully !')
            return redirect(register)
        else:
            messages.success(request, f'Could not create new account. Something went wrong')
            return render(request, 'registerUNO.html', {'form': form})
    return render(request, 'registerUNO.html', {'form': form})
