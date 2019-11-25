from django.shortcuts import render
from django.http import HttpResponse


def fa_dashboard(request):
    return render(request, "field-agent-dashboard.html")


def register_farmer(request):
    return render(request, "field-agent-farmer.html")


def survey(request):
    return render(request, "field-agent-survey.html")
