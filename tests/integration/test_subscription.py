import pytest

def test_create_subscription(builton_user):
    subscription = builton_user.subscription().create(plan="5d975251d61310000bbbb68f", subscription_method="license")
    assert subscription.status == 'CREATED'

def test_start_subscription(builton_user):
    subscription = builton_user.subscription("5d97546cd61310000d1ba196").start(
        body={
            "payment_method": "5d96096b61a18e000f7d9fd1"
        }
    )
    assert subscription.status == 'ACTIVE'

def test_stop_subscription(builton_user):
    subscription = builton_user.subscription("5d97546cd61310000d1ba196").stop()
    assert subscription.status == 'NON_RENEWING'

def test_subscription_get_payments(builton_user):
    subscription = builton_user.subscription("5d97546cd61310000d1ba196")
    subscription.update(payment_method="5d96096b61a18e000f7d9fd1")
    payments = subscription.get_payments()
    assert isinstance(payments, list)
