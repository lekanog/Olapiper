from rest_framework.views import APIView
from datetime import datetime, timedelta, date
from rest_framework.response import Response
from utils.api_helper import response_maker, request_data_normalizer
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from .serializer import PaymentSerializer
from django.shortcuts import render,redirect,get_object_or_404
from .models import Payment
from Paymenthistory.models import Paymenthistory
from Paymentmethod.models import Card
from django.utils import timezone
from dateutil.relativedelta import relativedelta

def get_user(request):
	user = request.user
	if not (user.is_authenticated and user.is_active):
		return None
	return user


class PaymentView(APIView):
    def post(self, request):
        today = timezone.now().date()
        data = dict(request.data)
        pmethod = Card.objects.filter(id = data.get('method')).first()
        # Retrieve payment details from request data
        login_auth_user = get_user(request)
        amount = data.get('amount')
        item_id = data.get('item_id')
        item = data.get('item')
        frequency = data.get('frequency')
        user = login_auth_user
        method = pmethod
        last_paid = date.today()
        created = date.today()

        # Create a new payment object in the database
        if frequency == 'monthly':
            next_due = last_paid + timedelta(days=30)
        elif frequency == 'weekly':
            next_due = last_paid + timedelta(days=7)
        elif frequency == 'yearly':
            next_due = last_paid + timedelta(days=365)
        payment = Payment.objects.create(
            user=user,
            item_id=item_id,
            item = item,
            amount=amount,
            frequency=frequency,
            method = method,
            is_paid=False,
            last_paid = last_paid,
            next_due = next_due,
            created = created,
        )

        # Process the payment using the Preferred API
        try:
            payment.status = 'paid'
            print("Status")

            print("Status") 
            payment.is_paid = True
            payment.save()

            history = Paymenthistory.objects.create(
                 user = user,
                 Payment = payment,
                 amount = amount,
                 status = 'completed'

            )
            history.save()
            return Response(response_maker(response_type='success',
                message="You have successfully completed this payment!"),
                status=HTTP_200_OK
            )
        except:
            payment.status = 'failed'
            print("Status")

            print("Status") 
            payment.save()
            # Handle errors with the payment card
            history = Paymenthistory.objects.create(
                 user = user,
                 Payment = payment,
                 amount = amount,
                 status = 'failed'

            )
            return Response(response_maker(response_type='error',
                message="Error occured while processing payment!"),
            )
        
class Terminatepayment(APIView):
    def post(self, request,payment_id):
        specific_payment = Payment.objects.all()
	
        today = timezone.now().date()
        # Retrieve payment details from request data
        instance = get_object_or_404(Payment,id = payment_id)


        try:
            instance.status = 'terminated'
            instance.terminated_date = date.today()
            instance.save()
            return Response(response_maker(response_type='success',
                message="You have successfully terminated this payment!"),
                status=HTTP_200_OK
            )
        except:
            return Response(response_maker(response_type='error',
                message="Bad Request!"),
                status=HTTP_400_BAD_REQUEST
            )

class Paymentdetails(APIView):
    def get(self, request):
        payments = Payment.objects.filter(user=request.user).order_by('-created')
        serializer = PaymentSerializer(payments, many=True)
        return Response(response_maker(response_type='success',
                message="History gotten successfully",
                data=serializer.data),
                status=HTTP_200_OK
            )
    
class AllPaymentdetails(APIView):
    def get(self):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(response_maker(response_type='success',
                message="History gotten successfully",
                data=serializer.data),
                status=HTTP_200_OK
            )

# @periodic_task(run_every=timedelta(days=1))
# def process_recurring_payments():
#     today = timezone.now().date()
#     payments = Payment.objects.filter(status='due', last_failed__lt=today-timedelta(days=7))

#     for payment in payments:
#         try:
#             # charge = stripe.Charge.create(
#             #     amount=int(payment.amount * 100),
#             #     currency="usd",
#             #     source=payment.token,
#             #     description=payment.item
#             # )
#             payment.last_paid = timezone.now()

#             if payment.frequency == 'monthly':
#                 payment.next_due = payment.last_paid + relativedelta(months=1)
#             elif payment.frequency == 'weekly':
#                 payment.next_due = payment.last_paid + relativedelta(weeks=1)
#             elif payment.frequency == 'yearly':
#                 payment.next_due = payment.last_paid + relativedelta(years=1)

#             if payment.next_due <= today:
#                 payment.next_due = today

#             payment.status = 'paid'
#             payment.save()

#         except:
#             payment.last_failed = timezone.now()
#             payment.status = 'due'
#             payment.save()

#     # Reset payment status for recurring payments that are now due
#     Payment.objects.filter(status='paid', next_due__lt=today, frequency__isnull=False).update(status='due')