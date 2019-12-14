from django.urls import path, include

from UNO import views

urlpatterns = [
    path('', views.unoHome, name='unoHome'),
    path('registerFA', views.register, name='registerFA'),
    path('profile',views.profile,name='profile'),
    path('profile-edit', views.unoUpdate, name = 'unoUpdate'),
    path('logout', views.logout, name = 'logout'),
    path('surveylist',views.show,name='surveylist')
]
