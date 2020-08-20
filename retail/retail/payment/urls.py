from django.urls import include, path, re_path
from .views import (
    get_or_post_payment_gateway
)


urlpatterns = [
    path('app/get_or_post_payment_gateway',
         get_or_post_payment_gateway.as_view(), name='post_payment_data')
]
