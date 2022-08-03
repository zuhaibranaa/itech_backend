from django.shortcuts import render
from requests import delete
from rest_framework.views import APIView,Response,status
from .serializers import *
from .models import *
# Create your views here.

class InvoicesView(APIView):
    # get all invoices
    def get(self,request):
        data = Invoice.objects.all()
    # get single invoice
    def patch(self,request):
        pass
    # update an invoice
    def put(self,request):
        pass
    # create new invoice
    def post(self,request):
        pass
    # delete an invoice
    def delete(self,request):
        pass

class PaymentsView(APIView):
    #  get all payments
    def get(self,request):
        data = Payments.objects.all()
        serializer = PaymentSerializer(data=data,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    # get single payment
    def patch(self,request):
        data = Payments.objects.get(invoice = request.invoice)
        serializer = PaymentSerializer(data=data)
        return Response(serializer.data,status.HTTP_200_OK)
    # update a payment
    def put(self,request):
        pass
    # create new payment
    def post(self,request):
        pass
    # delete a payment
    def delete(self,request):
        pass