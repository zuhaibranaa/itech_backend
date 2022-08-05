from django.shortcuts import render
from requests import delete
from rest_framework.views import APIView,status
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.

class InvoicesView(APIView):
    # get all invoices
    def get(self,request):
        data = Invoice.objects.all()
        serializer = InvoiceSerializer(data=data,many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data,status.HTTP_200_OK)
        except:
            return Response({'error':'Data Has Errors'})
    # get single invoice
    def patch(self,request):
        data = Invoice.objects.get(id=request.data.id)
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid(True):
            return Response(serializer.data,status.HTTP_200_OK)
        
    # update an invoice
    def put(self,request):
        pass
    # create new invoice
    def post(self,request):
        invoice = InvoiceSerializer(data=request.data)
        if invoice.is_valid(True):
            invoice.save()
            return Response(invoice.data,status.HTTP_201_CREATED)
            
    # delete an invoice
    def delete(self,request):
        print(request.data.get('id'))
        data = Invoice.objects.get(id = request.data.get('id'))
        try:
            data.delete()
            return Response({'message': 'Object Deleted Successfully'},status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Error Deleting Object'},status.HTTP_204_NO_CONTENT)
            

class PaymentsView(APIView):
    #  get all payments
    def get(self,req):
        data = Payments.objects.all()
        serializer = PaymentSerializer(data=data,many=True)
        if serializer.is_valid(True):
            return Response(serializer.data,status.HTTP_200_OK)
    # get single payment
    def patch(self,request):
        data = Payments.objects.get(id = request.payment)
        serializer = PaymentSerializer(data=data)
        return Response(serializer.data,status.HTTP_200_OK)
    # update a payment
    def put(self,request):
        data = Payments.objects.get(id = request.payment)
        serializer = PaymentSerializer(data=data)
        return Response(serializer.data,status.HTTP_200_OK)
    # create new payment
    def post(self,request):
        payment = Payments.objects.create(request)
        serializer = PaymentSerializer(payment) 
        if serializer.is_valid():
            payment.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
    # delete a payment
    def delete(self,request):
        print(request)
        data = Payments.objects.filter(request.data.id)
        data.delete()
        return Response({'message': 'Object Deleted Successfully'},status.HTTP_204_NO_CONTENT)