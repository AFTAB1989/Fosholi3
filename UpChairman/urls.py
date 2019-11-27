from django.urls import path, include

from UNO import views

urlpatterns = [
    path('', views.show, name='UpChairmanhomeDisplay'),
    #  path('uno_reg', views.uno_reg, name='uno_register'),
]
