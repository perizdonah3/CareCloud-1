
from django.contrib import admin
from django.urls import path
from careapp import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home,name='index.html'),
    path('starter/', views.starter,name='starter-page.html'),
]
