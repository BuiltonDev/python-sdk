from random import randint

from builton_sdk import Builton
from config import *


builton = Builton(endpoint=ENDPOINT, api_key=API_KEY, bearer_token=BEARER_TOKEN)

company = builton.company().get()
print(company.name)

users = builton.user().get_all()
print(users)

user = users[0]
user_id = user.id
print(user)
print(user_id)

user = builton.user().get(user_id)
print(user)
print(user.first_name)

user = user.update(first_name='test%s' % randint(1, 100))
print(user)
print(user.first_name)

product = builton.product().create(name="Nike Air",
                                   description="Just do it!",
                                   price=1000,
                                   currency="NOK")
product.delete()
product = builton.product().get(id=product.id)
print(product.deleted)

orders = builton.order().get_all()
print(orders)

orders = builton.order().get_all(json=True)
print(orders)

order = builton.order(orders[0]).refresh()
print(order)


