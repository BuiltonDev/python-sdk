import pytest

from builton_sdk.api_models import Product


def test_get_products_has_attributes_with_right_types(builton):
    products = builton.product().get_all()

    assert isinstance(products, list)
    for product in products:
        assert isinstance(product, Product)
        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.short_description, str)
        assert isinstance(product.currency, str)
        assert isinstance(product.company, dict)
        assert isinstance(product.price, float)
        assert isinstance(product.price_change_percentage, float)
        assert isinstance(product.vat, float)
        assert isinstance(product.tags, list)
        assert isinstance(product.human_id, str)
        assert isinstance(product.main_product, bool)
        assert isinstance(product.parents, list)
        assert isinstance(product.properties, dict)


def test_get_product(builton):
    products = builton.product().get_all()
    assert isinstance(products, list)

    product_id = products[0].id

    product = builton.product().get(id=product_id)
    assert isinstance(product, Product)


