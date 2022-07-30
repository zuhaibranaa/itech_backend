from django.shortcuts import render
from rest_framework.views import APIView,Response

# Create your views here.
class User(APIView):
    def get(self,request):
        return Response({'data': request.headers},200)