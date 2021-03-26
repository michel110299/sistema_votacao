from django.contrib import admin
from django.urls import path , include
from cadastro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cadastro/',include('cadastro.urls')),
    path('adm/',include('adm_votocao.urls')),
    path('',include('home.urls')),
]
