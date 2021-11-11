from django.contrib import admin
from django.urls import path
from userms.views import *
from django.urls import path, include

app_name = 'userms'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]
