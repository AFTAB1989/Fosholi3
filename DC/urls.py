from django.urls import path, include

from DC import views

urlpatterns = [
    path('', views.show, name='DChomeDisplay'),
    path('register', views.register, name='upcregister'),
    #  path('upc_reg', views.upc_reg, name='homeToLogin'),
]
