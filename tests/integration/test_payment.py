import pytest

def test_order_payment(builton_user):
    payment_method = builton_user.payment_method().get("5d96096b61a18e000f7d9fd1")

    order = builton_user.order().get("5d97406ad6131000103999df")

    payments = builton_user.payment().pay(body={
        "orders": [order.id],
        "payment_method": payment_method.id
    })
    assert payments[0].current_state == "succeeded"

def test_multiple_order_payment(builton_user):
    payment_method = builton_user.payment_method().get("5d96096b61a18e000f7d9fd1")

    order = builton_user.order().get("5d97406ad6131000103999df")

    payments = builton_user.payment().pay(body={
        "orders": ["5d9b04412cc5f4000ca9e4d6", "5d97406ad6131000103999df"],
        "payment_method": payment_method.id
    })
    assert payments[0].current_state == "succeeded"
    assert payments[1].current_state == "succeeded"
