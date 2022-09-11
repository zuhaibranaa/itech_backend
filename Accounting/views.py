from rest_framework.response import Response
from rest_framework.views import APIView, status
from .serializers import *
from itech_backend.settings import MEDIA_URL


def check_status(status):
    if status:
        return 'Active'
    return "Inactive"


# Create your views here.
class SuppliersView(APIView):
    # get all Suppliers
    def get(self, request):
        data = Supplier.objects.all()
        serializer = SupplierSerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Data Has Errors'})

    # get single Supplier
    def patch(self, request):
        try:
            data = Supplier.objects.get(id=request.data.get('id'))
            return Response({
                'id': data.id,
                'name': data.name,
                'email': data.email,
                'address': data.address,
                'mobile': data.mobile,
            }, status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': "No Record Found Against Provided Id"}, status.HTTP_404_NOT_FOUND)

    # update a Supplier

    def put(self, request):
        data = Supplier.objects.get(id=request.data.get('id'))
        data.name = request.data.get('name')
        data.email = request.data.get('email')
        data.address = request.data.get('address')
        data.mobile = request.data.get('mobile')
        data.save()
        return Response({
            'id': data.id,
            'name': data.name,
            'email': data.email,
            'address': data.address,
            'mobile': data.mobile,
        }, status.HTTP_200_OK)

    # create new Supplier
    def post(self, request):
        supplier = SupplierSerializer(data=request.data)
        if supplier.is_valid(True):
            supplier.save()
            return Response(supplier.data, status.HTTP_201_CREATED)
        return Response({'message': "Data Has Errors Try Again"}, status.HTTP_400_BAD_REQUEST)

    # delete a Supplier
    def delete(self, request):
        try:
            data = Supplier.objects.get(id=request.data.get('id'))
            data.delete()
            return Response({'message': 'Object Deleted Successfully'}, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)


# pending Invoice Update Method
class InvoicesView(APIView):
    # get all invoices
    def get(self, request):
        data = Invoice.objects.all()
        serializer = InvoiceSerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Data Has Errors'})

    # get single invoice
    def patch(self, request):
        data = Invoice.objects.get(id=request.data.get('id'))
        print(MEDIA_URL + str(data.customer.image.name))
        return Response({
            'id': data.id,
            'billing_date': data.billing_date,
            'due_date': data.due_date,
            'discount': data.discount,
            'other_dues': data.other_dues,
            'total_amount': data.total_amount,
            'created_at': data.created_at,
            'updated_at': data.updated_at,
            'customer': {
                "id": data.customer.id,
                "name": data.customer.name,
                "email": data.customer.email,
                "image": MEDIA_URL + str(data.customer.image.name),
                "location": data.customer.location,
                "cnic": data.customer.cnic,
                "phone": data.customer.phone,
                "status": check_status(data.customer.is_active),
                "pppoe": data.customer.pppoe.name,
                "profile": data.customer.profile.name,
            },
            'generated_by': {
                "id": data.generated_by.id,
                "name": data.generated_by.name,
                "email": data.generated_by.email,
                "image": MEDIA_URL + str(data.generated_by.image.name),
                "location": data.generated_by.location,
                "cnic": data.generated_by.cnic,
                "phone": data.generated_by.phone,
            },
            'description': data.description,
            'status': data.invoice_status,
        }, status.HTTP_200_OK)

    # update an invoice
    def put(self, request):
        data = Invoice.objects.get(id=request.data.get("invoice"))
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
        except Exception as e:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)


class JournalView(APIView):
    # get all invoices
    def get(self, request):
        data = Journal.objects.all()
        serializer = JournalSerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Data Has Errors'})

    # get single invoice
    def patch(self, request):
        data = Journal.objects.get(id=request.data.id)
        serializer = JournalSerializer(data=data)
        if serializer.is_valid(True):
            return Response(serializer.data, status.HTTP_200_OK)

    # update an invoice
    def put(self, request):
        data = Journal.objects.get(id=request.data.payment)
        serializer = JournalSerializer(data=data)
        return Response(serializer.data, status.HTTP_200_OK)

    # create new invoice
    def post(self, request):
        journal = JournalSerializer(data=request.data.get('description'))
        if journal.is_valid():
            print(' Journal Saved')
            journal.save()
        j_rec = Journal.objects.get(description=request.data.get('description'))
        transactions_data = request.data.get('transactions')
        for obj in transactions_data:
            obj['journal_entry_id'] = j_rec.id
        print(transactions_data)
        # transactions = TransactionSerializer(data=request.data.get('transactions'), many=True)
        # transactions.is_valid()
        # print(transactions.data)
        #     return Response(journal.data, status.HTTP_201_CREATED)

    # delete an invoice
    def delete(self, request):
        data = Journal.objects.get(id=request.data.get('id'))
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
