from django.contrib import messages
from django.shortcuts import render, redirect

from FieldAgent import models
from FieldAgent.models import SeasonalServey
from UNO.forms import RegisterForm


def faList(request):
    allFa = models.FieldAgent.objects.all()
    return render(request, 'uno-agent.html', {'agentList': allFa})


# UNO registering FA
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)  # saves from data in model
            messages.success(request, f'New Field Agent added successfully !')
            return redirect(register)
        else:
            messages.error(request, f'Could not create new account. Something went wrong')
            return render(request, 'registerFA.html', {'form': form})
    return render(request, 'registerFA.html', {'form': form})


def surveyReport(request):
    # if request.POST.get("submit2_uno"):
        s = SeasonalServey.objects.all()
        return render(request, 'surveyReport.html', {'surveylist': s})