from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('nas/',view=NAS_Crud.as_view())
]