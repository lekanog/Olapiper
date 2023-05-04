from rest_framework import serializers

from .models import Paymenthistory
from users.models import Users
from Payment.models import Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    Payment = PaySerializer()
    class Meta:
        model = Paymenthistory
        fields = '__all__'