from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.fa_dashboard, name='fa_Dashboard'),
    path('register_farmer/', views.register_farmer, name='fa_register_farmer'),
    path('survey/', views.survey, name='fa_survey'),
]