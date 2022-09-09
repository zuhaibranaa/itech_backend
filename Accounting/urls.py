from django.urls import path
from .views import *

urlpatterns = [
    path('invoices/', view=InvoicesView.as_view()),
    path('suppliers/', view=SuppliersView.as_view()),
    path('payments/', view=PaymentsView.as_view()),
    path('sales/', view=SalesView.as_view()),
    path('inventory/', view=InventoryView.as_view()),
    path('journal/', view=JournalView.as_view())
]
