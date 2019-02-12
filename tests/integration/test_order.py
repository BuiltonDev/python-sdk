import pytest

from src.main import Kvass
from src.collection.order import Order
from tests.integration.config import ENDPOINT, API_KEY, BEARER_TOKEN


@pytest.fixture
def kvass():
    return Kvass(endpoint=ENDPOINT,
                 api_key=API_KEY,
                 bearer_token=BEARER_TOKEN)


def test_get_orders_has_attributes_with_right_types(kvass):
    orders = kvass.order().get_all()

    assert isinstance(orders, list)

    for order in orders:
        assert isinstance(order, Order)
        assert isinstance(order.currency, str)
        assert isinstance(order.deliveries, list)
        assert isinstance(order.delivery_status, str)
        assert isinstance(order.order_status, str)
        assert isinstance(order.items, list)
        assert isinstance(order.human_id, str)
        assert isinstance(order.note, str)
        assert isinstance(order.payments, list)
        assert isinstance(order.resources, list)
        assert isinstance(order.top_up_amount, int)
        assert isinstance(order.top_up_vat, float)
        assert isinstance(order.total_amount, (int, float))
        assert isinstance(order.total_quantity, int)
        assert isinstance(order.units, int)
        assert isinstance(order.stripe_charge_id, str)
        assert isinstance(order.stripe_refund_id, str)
