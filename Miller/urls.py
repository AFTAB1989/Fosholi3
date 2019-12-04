from django.urls import path, include

from Miller import views

urlpatterns = [
    path('', views.show, name='millerhome'),
]
