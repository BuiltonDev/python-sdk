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

    order = builton.order(order_id).get()
    assert isinstance(order, Order)
