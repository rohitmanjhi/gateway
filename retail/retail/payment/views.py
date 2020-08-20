from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from retail.payment.models import Card, CardType, Currency, Status, PaymentGateway
from retail.payment.serializers import PaymentGatewaySerializer, CardSerializer
# Create your views here.


class get_or_post_payment_gateway(APIView):

    def post(self, request):
        # Get all requested data
        request_payload = request.data
        response_payload = {}

        # Get Currency instance
        try:
            currency = Currency.objects.get(name=request_payload['currency'])
        except:
            response_payload['errors'] = "Currency not exist"
            response_payload['status'] = "failed"
            return Response(response_payload, content_type="application/json")

        # Get Card type instance
        try:
            card_type = CardType.objects.get(name=request_payload['type'])
        except:
            response_payload['errors'] = "Card type not exist"
            response_payload['status'] = "failed"
            return Response(response_payload, content_type="application/json")

        # insert Card related data in dictionary
        card_data = {}
        card_data['number'] = request_payload['card']['number']
        card_data['expiration_month'] = request_payload['card']['expirationMonth']
        card_data['expiration_year'] = request_payload['card']['expirationYear']
        card_data['cvv'] = request_payload['card']['cvv']

        card_serializer = CardSerializer(data=card_data)
        # Check card serializer valid or not
        if card_serializer.is_valid():
            card = card_serializer.save()
            print('card: ', card)
        else:
            response_payload['errors'] = card_serializer.errors
            response_payload['status'] = "failed"
            return Response(response_payload, content_type="application/json")

        # Get status instance
        try:
            status = Status.objects.get(name="success")
        except:
            response_payload['errors'] = "Status not found"
            response_payload['status'] = "failed"
            return Response(response_payload, content_type="application/json")

        # Payment related data insert in dictionary
        payment_data = {}
        payment_data['amount'] = request_payload['amount']
        payment_data['currency'] = currency.id
        payment_data['card_type'] = card_type.id
        payment_data['card'] = card.id
        payment_data['status'] = status.id

        payment_serializer = PaymentGatewaySerializer(data=payment_data)
        # Check payment serializer valid or not
        if payment_serializer.is_valid():
            payment_gateway = payment_serializer.save()
        else:
            response_payload['errors'] = payment_serializer.errors
            response_payload['status'] = "failed"
            return Response(response_payload, content_type="application/json")

        # response data insert in dictionary
        response_payload["amount"] = payment_gateway.amount
        response_payload["currency"] = payment_gateway.currency.name
        response_payload["type"] = card_type.name
        response_payload["card"] = ({"number": card.number})
        response_payload["status"] = payment_gateway.status.name
        response_payload["authorization_code"] = payment_gateway.authorization_code
        response_payload["time"] = payment_gateway.created_at.strftime(
            '%d-%m-%Y %H:%M:%S')

        return Response(response_payload, content_type="application/json")
