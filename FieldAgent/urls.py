from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.fa_dashboard, name='fa_Dashboard'),
    path('register_farmer/', views.register_farmer, name='fa_register_farmer'),
    path('survey/', views.addSurvey, name='fa_survey'),
    # path('survey/addSurvey', views.addSurvey, name='add_survey'),
    path('surveylist/', views.surveyList, name='add_survey'),
]