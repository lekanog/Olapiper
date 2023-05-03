from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Card
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.api_helper import response_maker
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from .serializer import CardSerializer

def get_user(request):
	user = request.user
	if not (user.is_authenticated and user.is_active):
		return None
	return user



class CardHistory(APIView):
    def get(self, request):
        payments = Card.objects.filter(user=request.user)
        serializer = CardSerializer(payments, many=True)
        return Response(response_maker(response_type='success',
                message="History gotten successfully",
                data=serializer.data),
                status=HTTP_200_OK
            )
    

class AddCardView(APIView):
    def post(self, request):
        # Retrieve card details from request data
        name_on_card = request.data.get('name_on_card')
        card_number = request.data.get('card_number')
        expiration_date = request.data.get('expiration_date')
        security_code = request.data.get('security_code')
        user = request.user

        # Create a new card object in the database
        card = Card.objects.create(
            user=user,
            name_on_card=name_on_card,
            card_number=card_number,
            expiration_date=expiration_date,
            security_code=security_code
        )
        # serializer = CardSerializer(card, many=True)
        card.save()
        return Response(response_maker(response_type='success',
        message="Card Added successfully"),
        status=HTTP_200_OK
            )
