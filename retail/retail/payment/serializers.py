from rest_framework import serializers
from retail.payment.models import PaymentGateway, Card


class PaymentGatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentGateway
        fields = '__all__'

    # def validate_mobile(self, mobile):
    #     if re.match(r'[6789]\d{9}$', mobile):
    #         return mobile
    #     else:
    #         raise serializers.ValidationError(
    #             "Please enter valid mobile number")


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
