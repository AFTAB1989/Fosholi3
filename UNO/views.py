from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from UNO.forms import RegisterForm


def show(request):
    return render(request, 'uno-agent.html')


# UPC registering UNO page
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)  # saves from data in model
            messages.success(request, f'New Field Agent added successfully !')
            return redirect(register)
        else:
            messages.success(request, f'Could not create new account. Something went wrong')
            return render(request, 'registerFA.html', {'form': form})
    return render(request, 'registerFA.html', {'form': form})
