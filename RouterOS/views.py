from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests.auth import HTTPBasicAuth
from rest_framework import status
from RouterOS.models import *
from .serializers import NasSerializer, ProfileGroupSerializer
from rest_framework import viewsets
from rest_framework.permissions import *
# Create your views here.

class NAS_Crud(APIView):
    # creating new NAS
    def post(self,request):
        # nas = NAS()
        # print(request.data)
        api_data = requests.get(url='https://192.168.88.1/rest/ppp/profile',auth=HTTPBasicAuth('admin', 'password'),verify=False)
        if api_data.status_code == 200:
            return Response({'data':'NAS Added Successfully'})
        else:
            return Response({'error':'NAS Registration Failed Check Your API Or Credentials'},status.HTTP_400_BAD_REQUEST)
    # updating a NAS
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
    
class PPPOE_View(APIView):
    def get(self,req):
        obj = NAS.objects.all()
        serializer = NasSerializer(obj,many=True)
        data = []
        for o in serializer.data:
            data.append(requests.get(url='https://'+o.get('ip_address')+'/rest/ppp/secret',auth=HTTPBasicAuth(o.get('username'), o.get('password')),verify=False).json())
        return Response(data,status=status.HTTP_200_OK)
    
class Profile(APIView):
    def get(self,request):
        obj = NAS.objects.all()
        serializer = NasSerializer(obj,many=True)
        data = []
        for o in serializer.data:
            ip = o.get('ip_address')
            data.append(requests.get(url=f'https://{ip}/rest/ppp/profile',auth=HTTPBasicAuth(o.get('username'), o.get('password')),verify=False).json())
        return Response(data,status=status.HTTP_200_OK)
class ProfileGroupView(APIView):
    def get(self,request):
        obj = ProfileGroup.objects.all()
        serializer = ProfileGroupSerializer(data=obj,many=True)
        if serializer.is_valid():
            return Response(serializer.data,status.HTTP_200_OK)