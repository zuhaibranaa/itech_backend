from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from Accounting.serializers import BillingAccountSerializer
from Accounting.models import BillingAccounts
from django.contrib.auth import authenticate
from rest_framework.parsers import MultiPartParser, FormParser


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


class UserRegister(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            serializer = UserProfileSerializer(user)
            user_account = BillingAccountSerializer(data={'user': serializer.data.id, 'current_balance': 0})
            if user_account.is_valid():
                user_account.save()
            return Response({'user': serializer.data, 'token': token, 'user_account': user_account.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        pass


class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            e_mail = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=e_mail, password=password)
            if user is not None:
                user_account = BillingAccounts.objects.get(user=user.data.id)
                token = get_tokens_for_user(user)
                serializer = UserProfileSerializer(user)
                return Response({'user': serializer.data, 'token': token}, status.HTTP_202_ACCEPTED)
            else:
                return Response({'error': 'No User Found Against Your Email Or Password Check Your Credentials'},
                                status.HTTP_404_NOT_FOUND)


class GetCustomers(APIView):
    def get(self, req):
        objects = User.objects.filter(roles_id=0)
        serializer = UserProfileSerializer(data=objects, many=True)
        serializer.is_valid()
        return Response(serializer.data, status.HTTP_200_OK)
