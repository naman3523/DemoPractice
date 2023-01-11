from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('bulk',views.bulk,name='bulk'),
    path('query',views.query,name='query')
]