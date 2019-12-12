from django.contrib import messages
from django.db.models import Sum
from django.db.models import Count
from django.shortcuts import render, redirect

from FieldAgent.models import SeasonalServey
from UNO.models import UNO
from UpChairman.forms import RegisterForm


def show(request):
    return render(request, 'upcHome.html')


def unoList(request):
    allUno = UNO.objects.all()
    return render(request, 'allUno.html', {'unolist': allUno})


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


def surveyReportfrmUNO(request):
    total_survey = SeasonalServey.objects.count()
    sum_by_crop = SeasonalServey.objects.aggregate(Sum('estimatedCrop'))
    sum_farmed_land = SeasonalServey.objects.aggregate(Sum('areaOfFarmedLand'))
    estimation = SeasonalServey.objects.values('cropType').order_by('cropType').annotate(
        total_crop=Sum('estimatedCrop'))

    context = {'total_survey': total_survey, 'sum_by_crop': sum_by_crop, 'sum_farmed_land': sum_farmed_land,
               'estimation': estimation}

    return render(request, 'Surey_report_UPZ.html', context)
