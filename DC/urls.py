from django.urls import path, include

from DC import views

urlpatterns = [
    path('', views.show, name='DChomeDisplay'),
    path('register', views.register, name='upcregister'),
    path('allUPC/', views.upcList, name='showUPC'),
    path('surveyReportfrmUPC/', views.surveyReportfrmUPC, name='surveyReportfrmUPC'),
]
