from django.urls import path, include

from Farmer import views

urlpatterns = [
    path('', views.show, name='MainPage'),
    path('frmrLoggedIn', views.fHome, name='farmerHomeDisplay'),
    path('login_pg', views.login_pg, name='homeToLogin'),
]
