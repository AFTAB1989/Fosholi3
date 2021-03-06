from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

from FieldAgent.models import SeasonalServey


def fa_dashboard(request):
    return render(request, "field-agent-dashboard.html")


def register_farmer(request):
     # form = RegisterForm()
     
    # if request.method == "POST":
    #     form = RegisterForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save(commit=True)  # saves from data in model
    #         messages.success(request, f'New account created successfully !')
    #         return redirect(register)
    #     else:
    #         messages.success(request, f'Could not create new acount. Something went wrong')
    #         return render(request, 'registerChairman.html', {'form': form})
    # return render(request, 'registerChairman.html', {'form': form})
     return render(request, "field-agent-farmer.html")


def survey(request):
    return render(request, "field-agent-survey.html")


def addSurvey(request):
    if request.method == 'POST':
        s = SeasonalServey(surveyId=request.POST['sID'], fId=request.POST['fID'], seasonId=request.POST['seasonID'],
                           areaOfFarmedLand=request.POST['areaof'], farmedCrop=request.POST['fCrop'],
                           cropType=request.POST['cType'], estimatedCrop=request.POST['estCrop'],
                           farmingStartDate=request.POST['fStart'], farmingEndDate=request.POST['fEnd'])
        s.save()
        return redirect('/surveyList/')


def surveyList(request):
    s = SeasonalServey.objects.all()
    return render(request, 'allSurvey.html', {'surveylist': s})
    #return HttpResponse('<h1> hello survey</h1>')
