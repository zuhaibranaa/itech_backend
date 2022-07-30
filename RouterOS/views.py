import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from RouterOS.models import NAS
# Create your views here.

class NAS_Crud(APIView):
    def get(self,request):
        data = NAS.objects.all()
        return Response({'data': data},200)
    