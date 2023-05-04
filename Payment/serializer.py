from rest_framework import serializers
from Paymentmethod.models import Card
from .models import Payment
from users.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    method = CardSerializer()
    user = UserSerializer()
    class Meta:
        model = Payment
        fields = '__all__'