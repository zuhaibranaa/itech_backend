from rest_framework.response import Response
from rest_framework.views import APIView, status
from .serializers import *
from itech_backend.settings import MEDIA_URL


def check_status(status):
    if status:
        return 'Active'
    return "Inactive"


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


class InvoicesView(APIView):
    # get all invoices
    def get(self, request):
        data = Invoice.objects.all()
        serializer = InvoiceSerializer(data=data, many=True, source="i_status")
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Data Has Errors'})

    # get single invoice
    def patch(self, request):
        data = Invoice.objects.get(id=request.data.get('id'))
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
            'status': data.i_status(),
        }, status.HTTP_200_OK)

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
    # get all Entries
    def get(self, request):
        data = Journal.objects.all()
        objects = []
        for obj in data:
            transactions = Transaction.objects.filter(journal_entry_id=obj.id)
            list_of_transactions = [{
                    'id': t.id,
                    'type': t.tx_type,
                    'amount': t.amount,
                    'description': t.description,
                    't_account': t.t_account,
                    'account': {
                        'id': t.account.id,
                        'current_balance': t.account.current_balance,
                        'user': {
                            "id": t.account.user.id,
                            "name": t.account.user.name,
                            "email": t.account.user.email,
                            "image": MEDIA_URL + str(t.account.user.image.name),
                            "location": t.account.user.location,
                            "cnic": t.account.user.cnic,
                            "phone": t.account.user.phone,
                        },
                    },
                } for t in transactions]
            print(list_of_transactions)
            objects.append(
                {
                    'id': obj.id,
                    'date': obj.date,
                    'description': obj.description,
                    'activity_type': obj.activity_type,
                    'transactions': list_of_transactions
                }
            )
            return Response(objects, status.HTTP_200_OK)

    # get single Entry
    def patch(self, request):
        obj = Journal.objects.get(id=request.data.get('id'))
        transactions = Transaction.objects.filter(journal_entry_id=obj.id)
        list_of_transactions = [{
            'id': t.id,
            'type': t.tx_type,
            'amount': t.amount,
            'description': t.description,
            'account': {
                'id': t.account.id,
                'current_balance': t.account.current_balance,
                'user': {
                    "id": t.account.user.id,
                    "name": t.account.user.name,
                    "email": t.account.user.email,
                    "image": MEDIA_URL + str(t.account.user.image.name),
                    "location": t.account.user.location,
                    "cnic": t.account.user.cnic,
                    "phone": t.account.user.phone,
                },
            },
        } for t in transactions]
        return Response({
                    'id': obj.id,
                    'date': obj.date,
                    'description': obj.description,
                    'activity_type': obj.activity_type,
                    'transactions': list_of_transactions
                }, status.HTTP_200_OK)

    # create new Entry
    def post(self, request):
        if len(request.data.get('transactions')) < 2:
            return Response({'message': 'There Must Be Two Transactions'},status.HTTP_400_BAD_REQUEST)
        data = Journal.objects.create(
            description=request.data.get('description'),
            activity_type=request.data.get('type')
        )

        for t in request.data.get('transactions'):
            transaction = Transaction.objects.create(
                id=t.id,
                tx_type=t.tx_type,
                amount=t.amount,
                description=t.description,
                account_id=t.account_id,
                journal_entry_id=data.id,
                t_account=t.t_account
            )
            transaction.save()
        data.save()
        return Response({'message': 'Transactions And Journal Entry Saved'},status.HTTP_201_CREATED)

    # delete an Entry
    def delete(self, request):
        data = Journal.objects.get(id=request.data.get('id'))
        try:
            data.delete()
            return Response({'message': 'Object Deleted Successfully'}, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)


class InventoryView(APIView):
    # get all items
    def get(self, request):
        data = InventoryItem.objects.all()
        serializer = InventorySerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Data Has Errors'})

    # get single item
    def patch(self, request):
        try:
            data = InventoryItem.objects.get(id=request.data.get('id'))
            return Response({
                'id': data.id,
                'name': data.item_name,
                'price': data.purchase_price,
                'quantity': data.sku,
                'description': data.description,
                'buying_date': data.buying_date,
            }, status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': "No Data Found"})

    # Decrement or Increment in inventory items
    def put(self, request):
        try:
            data = InventoryItem.objects.get(id=request.data.get('id'))
            amount = 0
            if request.data.get('amount'):
                amount = int(request.data.get('amount'))
            if amount < 0:
                if data.sku >= amount:
                    data.sku -= amount
                    data.save()
            elif amount > 0:
                data.sku += amount
                data.save()
            else:
                data.delete()
            return Response({
                'id': data.id,
                'name': data.item_name,
                'price': data.purchase_price,
                'quantity': data.sku,
                'description': data.description,
                'buying_date': data.buying_date,
            }, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)

    # create new inventory item
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid(True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    # delete an Inventory
    def delete(self, request):
        try:
            data = InventoryItem.objects.get(id=request.data.get('id'))
            data.delete()
            return Response({"message": "Record Deleted Successfully"}, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': 'Error Deleting Object'}, status.HTTP_204_NO_CONTENT)


class SalesView(APIView):
    # get all invoices
    def get(self, request):
        data = Sale.objects.all()
        serializer = SalesSerializer(data=data, many=True)
        serializer.is_valid()
        try:
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Data Has Errors'})

    # create new invoice
    def post(self, request):
        sales = Sale.objects.create(
            quantity=request.data.get('quantity'),
            sale_price=request.data.get('price'),
            description=request.data.get('description'),
            customer_id=request.data.get('customer'),
            item_id=request.data.get('item_id'),
            payment_id=request.data.get('payment'),
        )
        sales.save()
        sales.item.sku -= request.data.get('quantity')
        sales.item.save()

        return Response({
            "quantity": sales.quantity,
            "sale_price": sales.sale_price,
            "description": request.data.get('description'),
            "customer": {
                "id": sales.customer.id,
                "name": sales.customer.name,
                "email": sales.customer.email,
                "image": MEDIA_URL + str(sales.customer.image.name),
                "location": sales.customer.location,
                "cnic": sales.customer.cnic,
                "phone": sales.customer.phone,
            },
            "item": {
                'id': sales.item.id,
                'name': sales.item.item_name,
                'price': sales.item.purchase_price,
                'quantity': sales.item.sku,
                'description': sales.item.description,
                'buying_date': sales.item.buying_date,
            },
                                                                        "payment_id": request.data.get('payment'),
        }, status.HTTP_201_CREATED)


class PaymentsView(APIView):
    #  get all payments
    def get(self, req):
        data = Payment.objects.all()
        serializer = PaymentSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data, status.HTTP_200_OK)

    # get single payment
    def patch(self, request):
        data = Payment.objects.get(id=request.data.get('id'))
        return Response({
            'id': data.id,
            'amount': data.amount,
            'method': data.method,
            'description': data.description,
            'created_at': data.created_at,
            'updated_at': data.updated_at,
            'invoice': {
                'id': data.invoice.id,
                'billing_date': data.invoice.billing_date,
                'due_date': data.invoice.due_date,
                'discount': data.invoice.discount,
                'other_dues': data.invoice.other_dues,
                'total_amount': data.invoice.total_amount,
                'created_at': data.invoice.created_at,
                'updated_at': data.invoice.updated_at,
            },
            'paid_by': {
                'id': data.paid_by.id,
                'current_balance': data.paid_by.current_balance,
                'user': {
                    "id": data.paid_by.user.id,
                    "name": data.paid_by.user.name,
                    "email": data.paid_by.user.email,
                    "image": MEDIA_URL + str(data.paid_by.user.image.name),
                    "location": data.paid_by.user.location,
                    "cnic": data.paid_by.user.cnic,
                    "phone": data.paid_by.user.phone,
                },
            },
        }, status.HTTP_200_OK)

    # create new payment
    def post(self, request):
        payment = Payment.objects.create(
            amount=request.data.get('amount'),
            method=request.data.get('method'),
            description=request.data.get('description'),
            invoice_id=request.data.get('invoice'),
            paid_by_id=request.data.get('paid_by'),
        )
        payment.invoice.invoice_status = 'paid'
        payment.invoice.save()
        payment.paid_by.current_balance -= payment.amount
        payment.paid_by.save()
        payment.save()
        return Response({
            "id": payment.id,
            "amount": payment.amount,
            "method": payment.method,
            "description": payment.description,
            'invoice': {
                'id': payment.invoice.id,
                'billing_date': payment.invoice.billing_date,
                'due_date': payment.invoice.due_date,
                'discount': payment.invoice.discount,
                'other_dues': payment.invoice.other_dues,
                'total_amount': payment.invoice.total_amount,
                'created_at': payment.invoice.created_at,
                'updated_at': payment.invoice.updated_at,
            },
            'paid_by': {
                "id": payment.paid_by.id,
                "name": payment.paid_by.name,
                "email": payment.paid_by.email,
                "image": MEDIA_URL + str(payment.paid_by.image.name),
                "location": payment.paid_by.location,
                "cnic": payment.paid_by.cnic,
                "phone": payment.paid_by.phone,
                "status": check_status(payment.paid_by.is_active),
                "pppoe": payment.paid_by.pppoe.name,
                "profile": payment.paid_by.profile.name,
            },
        }, status.HTTP_201_CREATED)
