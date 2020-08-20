import json
from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client
from retail.payment.models import PaymentGateway, Card, CardType, Currency, Status
# Create your tests here.


# initialize the APIClient app
client = Client()


class CurrencyTest(TestCase):
    """ Test module for Currency model """

    def setUp(self):
        Currency.objects.create(name='Dollar')

    def test_currency(self):
        currency_dollar = Currency.objects.get(name='Dollar')
        self.assertEqual(
            currency_dollar.name, "Dollar")


class CardTypeTest(TestCase):
    """ Test module for Card type model """

    def setUp(self):
        CardType.objects.create(name='prepaidcard')

    def test_card_type(self):
        card_type_prepaid = CardType.objects.get(name='prepaidcard')
        self.assertEqual(
            card_type_prepaid.name, "prepaidcard")


class StatusTest(TestCase):
    """ Test module for Status model """

    def setUp(self):
        Status.objects.create(name='created')

    def test_status(self):
        status_created = Status.objects.get(name='created')
        self.assertEqual(
            status_created.name, "created")


class CardTest(TestCase):
    """ Test module for Card model """

    def setUp(self):
        Card.objects.create(number=123456, expiration_month=2,
                            expiration_year=2022, cvv=123)

    def test_card_type(self):
        card_verify = Card.objects.get(
            number=123456, expiration_month=2, expiration_year=2022, cvv=123)
        self.assertEqual(
            card_verify.number, 123456)
        self.assertEqual(
            card_verify.expiration_month, 2)
        self.assertEqual(
            card_verify.expiration_year, 2022)
        self.assertEqual(
            card_verify.cvv, 123)


class PaymentGatewayTest(TestCase):
    """ Test module for Card model """

    def setUp(self):
        currency = Currency.objects.create(name='Dollar')
        card_type = CardType.objects.create(name='prepaidcard')
        status = Status.objects.create(name='created')
        card = Card.objects.create(number=123456, expiration_month=2,
                                   expiration_year=2022, cvv=123)
        PaymentGateway.objects.create(
            amount=100, currency=currency, card_type=card_type, status=status, card=card)

    def test_payment_gateway(self):

        payment_gateway = PaymentGateway.objects.get(
            amount=100,  card_type__name="prepaidcard", currency__name="Dollar", status__name="created", card__number=123456)
        self.assertEqual(
            payment_gateway.card.number, 123456)
        self.assertEqual(
            payment_gateway.currency.name, "Dollar")
        self.assertEqual(
            payment_gateway.status.name, "created")
        self.assertEqual(
            payment_gateway.card_type.name, "prepaidcard")


class CreatePaymentGatewayTest(TestCase):
    """ Test module for inserting a value of new Payment Gateway  """

    def setUp(self):
        self.valid_payload = {
            "amount": "180.23",
            "currency": "INR",
            "type": "debitcard",
            "card": {
                "number": "4111111111111111",
                "expirationMonth": "2",
                "expirationYear": "2020",
                "cvv": "111"
            }
        }

    def test_create_valid_payment_gateway(self):
        response = client.post(
            reverse('post_payment_data'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
