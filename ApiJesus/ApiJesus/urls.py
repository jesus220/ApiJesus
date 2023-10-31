"""
URL configuration for ApiJesus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from api.views import *
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('',Home.as_view(),name='das'),
    path('index.html', index.as_view(), name='index'),
    #path('login.html', login.as_view(), name='login'),
    path('icons.html', icono.as_view(), name='ico'),
    path('blank.html', blank.as_view(), name='blank'),
    path('buttons.html', buttons.as_view(), name='buttons'),
    path('flot.html', flot.as_view(), name='flot'),
    path('forms.html', forms.as_view(), name='forms'),
    path('grid.html', grid.as_view(), name='grid'),
    path('morris.html', morris.as_view(), name='morris'),
    path('notifications.html', notifications.as_view(), name='notifications'),
    path('panels-wells.html', panels.as_view(), name='panels'),
    path('tables.html', tables.as_view(), name='tables'),
    path('typography.html', typography.as_view(), name='typography'),
    path('forgot-password.html', forgot.as_view(), name='forgot'),
    path('register/', views.register, name= 'register'),
    path('login/', LoginView.as_view(template_name="login.html"), name= 'login'),
    path('chart/', views.chart_view, name='chart_view'),
    #path('salir/', views.salir, name="salir"),
    
]
