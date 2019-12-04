
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Farmer.urls')),
    path('admin/', admin.site.urls),
    path('FieldAgent/', include('FieldAgent.urls')),
    path('Farmer/', include('Farmer.urls')),
    path('UNO/', include('UNO.urls')),
    path('UpChairman/', include('UpChairman.urls')),
    path('DC/', include('DC.urls')),
    path('Miller/', include('Miller.urls')),
]
