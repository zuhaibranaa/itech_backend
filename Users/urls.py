from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('customer/register',view=CustomerRegister.as_view()),
    path('manager/login',view=ManagerLogin.as_view()),
    path('customer/login',view=CustomerLogin.as_view()),
]