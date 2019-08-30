import pytest
import random

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
        assert isinstance(product.price, (float, int))
        assert isinstance(product.price_change_percentage, (float, int))
        assert isinstance(product.vat, (float, int))
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

    product = builton.product().get_all(size=1)[0]
    assert isinstance(product, Product)


def test_update_product(builton):
    product = builton.product().get_all()[0]

    new_description = "test Python SDK"
    product = product.update(description=new_description)
    assert new_description == product.description


def test_create_and_delete_product(builton):
    data = {
        "name": "NAND gate",
        "description": "Super fast!",
        "currency": "NOK",
        "price": 2.89
    }
    product = builton.product().create(**data)
    assert isinstance(product, Product)
    assert data['name'] == product.name

    product = builton.product().get(id=product.id)
    product = product.delete()
    assert True == product.deleted
    assert False == product.active


def test_search_product(builton):
    query = 'product'
    products = builton.product().search(query=query)
    for product in products:
        print(product.name)
        assert query in product.name.lower()


def test_search_product_json(builton):
    query = 'product'
    products = builton.product().search(query=query, json=True)
    assert isinstance(products, list)

    for product in products:
        assert isinstance(product, dict)
        assert query in product['name'].lower()


@pytest.mark.skip("run it manually")
def test_refresh_product(builton):
    product = builton.product().create(name="WoW Classic",
                                       description="Return to the origin",
                                       currency="NOK", price=13.90)
    assert isinstance(product, Product)

    new_price = round(random.uniform(100.0, 200.42), 2)
    product.update(price=new_price)
    assert new_price != product.price

    updated_product = product.refresh()
    assert new_price == updated_product.price


def test_search_expand(builton):
    product = builton.product().get(id="5d67c87ad661690e5f6250a6")
    assert len(product.company) == 1

    product = builton.product().get(id="5d67c87ad661690e5f6250a6", expand="company")
    assert len(product.company) > 1
    assert 'name' in product.company
