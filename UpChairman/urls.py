from django.urls import path, include

from UpChairman import views

urlpatterns = [
    path('', views.show, name='UpChairmanhomeDisplay'),
    path('registerUNO', views.register, name='registerUNO'),
    path('allUNO/', views.unoList, name='showUNO'),
    path('surveyReportfrmUNO/', views.surveyReportfrmUNO, name='surveyReportfrmUNO'),
]
