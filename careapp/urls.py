
from django.contrib import admin
from django.urls import path
from careapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.index),


    path('starter/', views.starter),
    path('appointment/', views.appointment, name='appointment'),

path('about/', views.about, name='about'),
path('show/', views.show, name='show.html'),
path('pay/', views.pay, name='pay.html'),
path('payment-result/', views.payment_result, name='payment_result'),
path('delete/<int:id>/', views.delete, name='delete_item'),
path('edit/<int:id>',views.edit),

 #Mpesa URLS
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('payment-result/', views.payment_result, name='payment_result'),
    path('transactions/', views.transactions_list, name='transactions'),
#Authentication
    path('', views.register, name='register'),
    path('login/', views.login_view , name='login'),

]