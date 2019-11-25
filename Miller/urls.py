from django.urls import path, include

from Farmer import views

urlpatterns = [
    path('', views.show, name='MillerhomeDisplay'),
]
