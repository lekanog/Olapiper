from rest_framework import serializers

from .models import Card
from users.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Card
        fields = '__all__'