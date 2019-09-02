import pytest

from builton_sdk.api_models import Order


def test_get_orders_has_attributes_with_right_types(builton):
    orders = builton.order().get_all()

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
        assert isinstance(order.top_up_amount, (int, float))
        assert isinstance(order.top_up_vat, (int, float))
        assert isinstance(order.total_amount, (int, float))
        assert isinstance(order.total_quantity, int)
        assert isinstance(order.units, int)
        assert isinstance(order.stripe_charge_id, str)
        assert isinstance(order.stripe_refund_id, str)


def test_get_specific_order(builton):
    orders = builton.order().get_all()
    order_id = orders[0].id

    order = builton.order().get(order_id)
    assert isinstance(order, Order)


def test_get_orders_with_size_url_param(builton):
    orders = builton.order().get_all(url_params={"size": 1})
    assert isinstance(orders, list)
    assert 1 == len(orders)


def test_get_orders_with_order_status_param(builton):
    orders = builton.order().get_all(order_status="CREATED", size=1)
    assert isinstance(orders, list)
    assert 1 == len(orders)

    order = orders[0]
    assert "CREATED" == order.order_status


def test_get_orders_with_delivery_status_param(builton):
    orders = builton.order().get_all(delivery_status="PENDING", size=1)
    assert isinstance(orders, list)
    assert 1 == len(orders)

    order = orders[0]
    assert "PENDING" == order.delivery_status


def test_get_orders_with_from_date_param(builton):
    orders = builton.order().get_all(from_date=0, size=1)
    assert isinstance(orders, list)
    assert 1 == len(orders)

    order = orders[0]
    assert 0 < order.created['$date']


def test_get_orders_with_from_date_param_in_the_future(builton):
    orders = builton.order().get_all(from_date=2 << 70)
    assert isinstance(orders, list)
    assert 0 == len(orders)


def test_get_orders_with_to_date_param(builton):
    orders = builton.order().get_all(to_date=1567172963)
    assert isinstance(orders, list)
    assert 10 == len(orders)


def test_update_order_order_status(builton):
    orders = builton.order().get_all(order_status="CREATED", size=1)
    assert isinstance(orders, list)
    assert 1 == len(orders)

    order = orders[0]
    assert "CREATED" == order.order_status

    order = order.update(order_status="CREATED")
    assert isinstance(order, Order)
    assert "CREATED" == order.order_status


def test_update_order_missing_field(builton):
    orders = builton.order().get_all(order_status="CREATED", size=1)

    assert isinstance(orders, list)
    assert 1 == len(orders)

    order = orders[0]
    assert "CREATED" == order.order_status

    updated_order = order.update(missing_field=True)
    assert isinstance(updated_order, Order)
    assert not hasattr(updated_order, "missing_field")
    assert not hasattr(order, "missing_field")


@pytest.mark.skip("run it manually, so the list of "
                  "orders doesn't grow indefinitely")
def test_create_order(builton):
    items = [{"product": "5b768cd4a39863000a62707b",
              "quantity": 1}]
    user = "5a2a837a9bb92800137cb16f"
    order = builton.order().create(items=items, user=user)
    assert isinstance(order, Order)
