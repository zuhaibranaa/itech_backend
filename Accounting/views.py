from rest_framework.response import Response
from rest_framework.views import APIView, status

from .serializers import *


# Create your views here.

class InvoicesView(APIView):
    # get all invoices
    def get(self, request):
        data = Invoice.objects.all()
        serializer = InvoiceSerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({'error': 'Data Has Errors'})

    # get single invoice
    def patch(self, request):
        data = Invoice.objects.get(id=request.data.id)
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid(True):
            return Response(serializer.data, status.HTTP_200_OK)

    # update an invoice
    def put(self, request):
        data = Invoice.objects.get(id=request.data.payment)
        serializer = InvoiceSerializer(data=data)
        return Response(serializer.data, status.HTTP_200_OK)

    # create new invoice
    def post(self, request):
        invoice = InvoiceSerializer(data=request.data)
        if invoice.is_valid(True):
            invoice.save()
            return Response(invoice.data, status.HTTP_201_CREATED)

    # delete an invoice
    def delete(self, request):
        data = Invoice.objects.get(id=request.data.get('id'))
        try:
            data.delete()
            return Response({'message': 'Object Deleted Successfully'}, status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)


class SuppliersView(APIView):
    # get all invoices
    def get(self, request):
        data = Supplier.objects.all()
        serializer = SupplierSerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({'error': 'Data Has Errors'})

    # get single invoice
    def patch(self, request):
        data = Supplier.objects.get(id=request.data.id)
        serializer = SupplierSerializer(data=data)
        if serializer.is_valid(True):
            return Response(serializer.data, status.HTTP_200_OK)

    # update an invoice
    def put(self, request):
        data = Supplier.objects.get(id=request.data.payment)
        serializer = SupplierSerializer(data=data)
        return Response(serializer.data, status.HTTP_200_OK)

    # create new invoice
    def post(self, request):
        supplier = SupplierSerializer(data=request.data)
        if supplier.is_valid(True):
            supplier.save()
            return Response(supplier.data, status.HTTP_201_CREATED)

    # delete an invoice
    def delete(self, request):
        data = Supplier.objects.get(id=request.data.get('id'))
        try:
            data.delete()
            return Response({'message': 'Object Deleted Successfully'}, status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)


class InventoryView(APIView):
    # get all items
    def get(self, request):
        data = InventoryItem.objects.all()
        serializer = InventorySerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({'error': 'Data Has Errors'})

    # get single item
    def patch(self, request):
        data = InventoryItem.objects.get(id=request.data.id)
        serializer = InventorySerializer(data=data)
        if serializer.is_valid(True):
            return Response(serializer.data, status.HTTP_200_OK)

    # update an inventory item
    def put(self, request):
        data = InventoryItem.objects.get(id=request.data.payment)
        serializer = InventorySerializer(data=data)
        return Response(serializer.data, status.HTTP_200_OK)

    # create new inventory item
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid(True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    # delete an Inventory
    def delete(self, request):
        data = InventoryItem.objects.get(id=request.data.get('id'))
        try:
            data.delete()
            return Response({'message': 'Object Deleted Successfully'}, status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)


class SalesView(APIView):
    # get all invoices
    def get(self, request):
        data = Sale.objects.all()
        serializer = SalesSerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({'error': 'Data Has Errors'})

    # get single invoice
    def patch(self, request):
        data = Sale.objects.get(id=request.data.id)
        serializer = SalesSerializer(data=data)
        if serializer.is_valid(True):
            return Response(serializer.data, status.HTTP_200_OK)

    # update an invoice
    def put(self, request):
        data = Sale.objects.get(id=request.data.payment)
        serializer = SalesSerializer(data=data)
        return Response(serializer.data, status.HTTP_200_OK)

    # create new invoice
    def post(self, request):
        sales = SalesSerializer(data=request.data)
        if sales.is_valid(True):
            sales.save()
            return Response(sales.data, status.HTTP_201_CREATED)

    # delete an invoice
    def delete(self, request):
        data = Sale.objects.get(id=request.data.get('id'))
        try:
            data.delete()
            return Response({'message': 'Object Deleted Successfully'}, status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)


class PaymentsView(APIView):
    #  get all payments
    def get(self, req):
        data = Payment.objects.all()
        serializer = PaymentSerializer(data=data, many=True)
        if serializer.is_valid(True):
            return Response(serializer.data, status.HTTP_200_OK)

    # get single payment
    def patch(self, request):
        data = Payment.objects.get(id=request.payment)
        serializer = PaymentSerializer(data=data)
        return Response(serializer.data, status.HTTP_200_OK)

    # update a payment
    def put(self, request):
        data = Payment.objects.get(id=request.payment)
        serializer = PaymentSerializer(data=data)
        return Response(serializer.data, status.HTTP_200_OK)

    # create new payment
    def post(self, request):
        payment = Payment.objects.create(request)
        serializer = PaymentSerializer(payment)
        if serializer.is_valid():
            payment.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    # delete a payment
    def delete(self, request):
        print(request)
        data = Payment.objects.filter(request.data.id)
        data.delete()
        return Response({'message': 'Object Deleted Successfully'}, status.HTTP_204_NO_CONTENT)
