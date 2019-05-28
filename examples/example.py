from random import randint

from builton_sdk import Builton
from config import *

k = Builton(endpoint=ENDPOINT, api_key=API_KEY, bearer_token=BEARER_TOKEN)
users = k.user().get_all()
print(users)
user = users[0]
user_id = user.id
print(user)
print(user_id)
user = k.user(user_id).get()
print(user)
print(user.first_name)
user = user.update(body={'first_name': 'test%s' % randint(1, 100)})
print(user)
print(user.first_name)
providers = k.provider().get_all()
print(providers)
orders = k.order().get_all()
print(orders)
orders = k.order().get_all(json=True)
print(orders)
order = k.order(orders[0]).refresh()
print(order)
