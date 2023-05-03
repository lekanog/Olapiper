from django.urls import path
# from django.contrib.auth import views as auth_views
from .import views




app_name='Payment'

urlpatterns = [
    path('createpayment/', views.PaymentView.as_view()),
    path('allpaymentview/', views.AllPaymentdetails.as_view()),
    path('paymentview/', views.Paymentdetails.as_view()),
    path('terminatepayment/<str:payment_id>/', views.Terminatepayment.as_view()),
]