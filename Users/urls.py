from django.urls import path

from .views import *

urlpatterns = [
    path('register', view=UserRegister.as_view()),
    path('login', view=UserLogin.as_view()),
    path('customers', view=GetCustomers.as_view()),
]
