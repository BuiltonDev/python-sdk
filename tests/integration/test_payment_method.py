import pytest
import requests
import json

from config import STRIPE_SK

def test_create_payment_method(builton_user):
    data = {
        'type': 'card',
        'card[number]': '4242424242424242',
        'card[exp_month]': '12',
        'card[exp_year]': '2020',
        'card[cvc]': '123'
    }
    response = requests.post('https://api.stripe.com/v1/payment_methods', data=data, auth=(STRIPE_SK, ''))
    stripeResponse = response.json()

    payment_method = builton_user.payment_method().create(payment_method="stripe", payment_method_id=stripeResponse["id"])
    assert payment_method.method == "stripe"

def test_list_payment_methods(builton_user):
    payment_methods = builton_user.payment_method().get_all()
    assert isinstance(payment_methods, list)
    payment_methods[-1].method == "stripe"
