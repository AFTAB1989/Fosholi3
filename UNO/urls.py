from django.urls import path, include

from UNO import views

urlpatterns = [
    path('', views.show, name='UNOhomeDisplay'),
    path('registerFA', views.register, name='registerFA'),
]
