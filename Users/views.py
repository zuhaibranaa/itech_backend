from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from Accounting.models import BillingAccount, Invoice
from django.contrib.auth import authenticate
from rest_framework.parsers import MultiPartParser, FormParser
import datetime
from itech_backend.celery import first_day_of_next_month


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
            serializer = UserProfileSerializer(data=user)
            serializer.is_valid()
            account = BillingAccount(user=user, current_balance=0)
            account.save()
            invoice = Invoice(
                billing_date=datetime.datetime.now(),
                due_date=first_day_of_next_month(datetime.datetime.now()),
                discount=0,
                other_dues=0,
                total_amount=request.data.get('amount'),
                generated_by=request.user,
                description='Initial Amount Payment For New Connection',
                customer=user,
                invoice_status='pending'
            )
            invoice.save()
            return Response({'user': serializer.data, 'token': token, 'balance': account.current_balance}, status=status.HTTP_201_CREATED)
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
                token = get_tokens_for_user(user)
                serializer = UserProfileSerializer(user)
                user_account = BillingAccount.objects.get(user=serializer.data.get('id'))
                return Response({'user': serializer.data, 'balance': user_account.current_balance, 'token': token}, status.HTTP_202_ACCEPTED)
            else:
                return Response({'error': 'No User Found Against Your Email Or Password Check Your Credentials'},
                                status.HTTP_404_NOT_FOUND)


class GetCustomers(APIView):
    def get(self, req):
        objects = User.objects.filter(is_admin=False, is_superuser=False)
        serializer = UserProfileSerializer(data=objects, many=True)
        serializer.is_valid()
        return Response(serializer.data, status.HTTP_200_OK)
