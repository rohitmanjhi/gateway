from django.db import models
# Create your models here.


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Currency(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=25)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class CardType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class Card(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.PositiveIntegerField()
    expiration_month = models.PositiveIntegerField()
    expiration_year = models.PositiveIntegerField()
    cvv = models.PositiveIntegerField()

    class Meta:
        managed = True

    def __str__(self):
        return str(self.number)


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class PaymentGateway(BaseModel):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(blank=True,
                                 null=True,
                                 max_digits=10,
                                 decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    card_type = models.ForeignKey(CardType, on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='payment_gateway_status',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True
                               )
    authorization_code = models.CharField(max_length=100, blank=True,
                                          null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.authorization_code

    def save(self, *args, **kwargs):
        self.authorization_code = "{}{}".format(
            'SDSD', self.card.number)
        super(PaymentGateway, self).save(*args, **kwargs)
