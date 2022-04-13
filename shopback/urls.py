
from sys import api_version
from django.contrib import admin
from django.urls import path, include
from pip import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
