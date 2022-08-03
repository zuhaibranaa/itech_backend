from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests.auth import HTTPBasicAuth
from rest_framework import status
from RouterOS.models import *
from .serializers import NasSerializer
from rest_framework import viewsets
from rest_framework.permissions import *
# Create your views here.

class NAS_Crud(APIView):
    permission_classes = [AllowAny]
    # creating new NAS
    def post(self,request):
        # nas = NAS()
        # print(request.data)
        api_data = requests.get(url='https://192.168.88.1/rest/ppp/profile',auth=HTTPBasicAuth('admin', 'password'),verify=False)
        if api_data.status_code == 200:
            return Response({'data':'NAS Added Successfully'})
        else:
            return Response({'error':'NAS Registration Failed Check Your API Or Credentials'},status.HTTP_400_BAD_REQUEST)
    # updating new NAS
    def put(self,request):
        pass
    # deleting a nas
    def delete(self,request):
        pass
    # getting all nas
    def get(self,request):
        obj = NAS.objects.all()
        serializer = NasSerializer(obj,many=True)
        return Response(serializer.data,200)
    
class Profile(APIView):
    def get(self,request):
        api_data = requests.get(url='https://192.168.88.1/rest/ppp/profile',auth=HTTPBasicAuth('admin', 'password'),verify=False)
        print(api_data.json())
        return Response(api_data.json(),status=status.HTTP_200_OK)