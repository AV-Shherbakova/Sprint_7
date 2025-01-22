import json
import requests
from constants import CUSTOMER_DATA, ORDER_DATA, URL_ORDER_CREATE, URL_GET_ORDER_LIST


def create_order(colors=None):
    order_data = {**CUSTOMER_DATA, **ORDER_DATA}
    if colors is not None:
        order_data["color"] = colors
    json_data = json.dumps(order_data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_ORDER_CREATE, data=json_data, headers=headers)
    return response

def get_order_list():
    response = requests.get(URL_GET_ORDER_LIST)
    order_list = response.json()
    return response