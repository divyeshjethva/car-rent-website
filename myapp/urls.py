"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('bindex/', views.bindex, name='bindex'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('cars/', views.cars, name='cars'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('singup/', views.singup, name='singup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('fpass/', views.fpass, name='fpass'),
    path('otp/', views.otp, name='otp'),
    path('newpass/', views.newpass, name='newpass'),
    path('cpass/', views.cpass, name='cpass'),
    path('uprofile/', views.uprofile, name='uprofile'),
    path('add/', views.add, name='add'),
    path('view/', views.view, name='view'),
    path('cdetails/<int:pk>', views.cdetails, name='cdetails'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
