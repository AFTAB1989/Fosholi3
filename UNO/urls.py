from django.urls import path, include

from UNO import views

urlpatterns = [
    path('', views.faList, name='UNOhomeDisplay'),
    path('registerFA/', views.register, name='registerFA'),
    path('surveyReport/', views.surveyReport, name='SurveyReport'),
]
