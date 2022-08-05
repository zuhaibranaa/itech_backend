from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('nas/',view=NAS_Crud.as_view()),
    path('profile/',view=Profile.as_view()),
    path('profilegroup/',view=ProfileGroupView.as_view()),
    path('pppoe/',view=PPPOE_View.as_view())
]