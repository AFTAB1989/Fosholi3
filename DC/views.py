from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect

# DC index page
from FieldAgent.models import SeasonalServey
from UpChairman.forms import RegisterForm
from UpChairman.models import UpChairman


def show(request):
    return render(request, 'DChome.html')


# dc login page
def login_pg(request):
    return render(request, 'upcReg.html')


def upcList(request):
    allUpc = UpChairman.objects.all()
    return render(request, 'allUPC.html', {'upcList': allUpc})


# dc chairman register page
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)  # saves from data in model
            messages.success(request, f'New account created successfully !')
            return redirect(register)
        else:
            messages.success(request, f'Could not create new acount. Something went wrong')
            return render(request, 'registerChairman.html', {'form': form})

    return render(request, 'registerChairman.html', {'form': form})


def surveyReportfrmUPC(request):
    total_survey = SeasonalServey.objects.count()
    sum_by_crop = SeasonalServey.objects.aggregate(Sum('estimatedCrop'))
    sum_farmed_land = SeasonalServey.objects.aggregate(Sum('areaOfFarmedLand'))
    estimation = SeasonalServey.objects.values('cropType').order_by('cropType').annotate(
        total_crop=Sum('estimatedCrop'))

    context = {'total_survey': total_survey, 'sum_by_crop': sum_by_crop, 'sum_farmed_land': sum_farmed_land,
               'estimation': estimation}

    return render(request, 'Surey_report_DC.html', context)
