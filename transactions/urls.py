from django.urls import path
from . import views


urlpatterns = [
    path('transactions/', views.TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/all/', views.TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<uuid:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction-delete'),
    path('transaction-summary/', views.TransactionSummaryView.as_view(), name='transaction-summary'),
    path('transactions/import-csv/', views.TransactionImportCSV.as_view(), name='import-transactions'),
]
