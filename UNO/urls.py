from django.urls import path, include

from UNO import views

urlpatterns = [
    path('', views.unoHome, name='unoHome'),
    path('registerFA', views.register, name='registerFA'),
    path('surveylist',views.show,name='surveylist')
]
