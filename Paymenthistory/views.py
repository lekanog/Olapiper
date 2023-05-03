from rest_framework.views import APIView
from rest_framework.response import Response
from utils.api_helper import response_maker
from rest_framework.status import (
    HTTP_200_OK
)
from .serializer import PaymentSerializer
from .models import Paymenthistory
def get_user(request):
	user = request.user
	if not (user.is_authenticated and user.is_active):
		return None
	return user


class PaymentHistoryView(APIView):
    def get(self, request):
        payments = Paymenthistory.objects.filter(user=request.user).order_by('-date')
        serializer = PaymentSerializer(payments, many=True)
        return Response(response_maker(response_type='success',
                message="History gotten successfully",
                data=serializer.data),
                status=HTTP_200_OK
            )
    
class AllPaymentHistoryView(APIView):
    def get(self):
        payments = Paymenthistory.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(response_maker(response_type='success',
                message="History gotten successfully",
                data=serializer.data),
                status=HTTP_200_OK
            )