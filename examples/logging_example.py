import logging

from builton_sdk import Builton
from config import *

logging.basicConfig()
requests_log = logging.getLogger("builton_sdk")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

builton = Builton(endpoint=ENDPOINT, api_key=API_KEY, bearer_token=BEARER_TOKEN)
print(builton.product().get_all({"size": 1}))
