from rest_framework import serializers
from retail.payment.models import PaymentGateway, Card


class PaymentGatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentGateway
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
