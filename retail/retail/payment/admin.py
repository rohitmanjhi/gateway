from django.contrib import admin
from .models import Card, CardType, Currency, Status, PaymentGateway
# Register your models here.


class StatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class CurrencyAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class CardTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Card)
admin.site.register(CardType, CardTypeAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(PaymentGateway)
