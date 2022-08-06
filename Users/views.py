from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.contrib.auth import authenticate

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

class UserRegister(APIView):
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            serializer = UserProfileSerializer(user)
            return Response({'user': serializer.data,'token':token},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            e_mail = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=e_mail,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                serializer = UserProfileSerializer(user)
                return Response({'user':serializer.data,'token':token},status.HTTP_202_ACCEPTED)
            else:
                return Response({'error': 'No User Found Against Your Email Or Password Check Your Credentials'},status.HTTP_404_NOT_FOUND)
            
