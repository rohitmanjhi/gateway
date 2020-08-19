from django.contrib import admin
from .models import Card, CardType, Currency, Status, PaymentGateway
# Register your models here.

admin.site.register(Card)
admin.site.register(CardType)
admin.site.register(Currency)
admin.site.register(Status)
admin.site.register(PaymentGateway)
