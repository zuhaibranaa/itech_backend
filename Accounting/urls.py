from django.urls import path
from .views import *

urlpatterns = [
    path('invoices/',view=InvoicesView.as_view()),
    path('payments/',view=PaymentsView.as_view())
]