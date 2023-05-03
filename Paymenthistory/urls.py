from django.urls import path
# from django.contrib.auth import views as auth_views
from .import views




app_name='Paymenthistory'

urlpatterns = [
    path('allpaymenthistory/', views.AllPaymentHistoryView.as_view()),
    path('paymenthistory/', views.PaymentHistoryView.as_view()),
]