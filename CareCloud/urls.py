
from django.contrib import admin
from django.urls import path,include
from careapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('careapp.urls')),
]
