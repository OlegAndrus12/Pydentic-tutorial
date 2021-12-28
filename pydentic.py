import mock
from pydantic import BaseModel, validator, ValidationError, Field
from datetime import date
from typing import List

DELIMITER_SIZE = 30

print("*" * DELIMITER_SIZE)
print("Pydentic as a data class")


# args always converted to given types
# comprehensive error messages
# auto-completion in most popular IDE, no guessing

class OrderPydentic(BaseModel):    
    order_id: int
    email_address: str # alias to change the name in json, exclude to exclude certain fields
    checkout_date: date
    phone_number: str
    tags: List[str]
    
    @validator('email_address')
    def email_address_validator(cls, val):
        if not "@" in val:
            raise ValueError("Invalid email")
        return val
    
class OrdersList(BaseModel):
    list_name: str
    orders: List[OrderPydentic]


order = OrderPydentic(**mock.get_mocked_order())
print(order)
print(order.order_id)

print("*" * DELIMITER_SIZE)
print("Parsing input")
data = """
        {   
            "order_id": 82, 
            "email_address": "zmartinez@example.com",
            "checkout_date": "2008-09-23",
            "phone_number": "9353830438",
            "tags": ["west", "save", "military"]
        }
        """

order = OrderPydentic.parse_raw(data)
print(order)
print(order.order_id)

print("*" * DELIMITER_SIZE)
print("Invalid data")

data = mock.get_mocked_order()
data["order_id"] = "slug"
data["checkout_date"] = "random string"
data["tags"] = {}
try:
    order = OrderPydentic(**data)
except ValidationError as e:
    print(e.json())
    
print("*" * DELIMITER_SIZE) 
print("Nesting")

orders = [mock.get_mocked_order() for i in range(2)]
orders[0]['order_id'] = "Asd"
try:
    data2 = OrdersList(**{"list_name" : "Silpo", "orders" : orders})
    print(data2.json())
except ValidationError as e:
    print(e.json())
    

print("*" * DELIMITER_SIZE)
orders = [mock.get_mocked_order() for i in range(2)]
try:
    data2 = OrdersList(**{"list_name" : "Silpo", "orders" : orders})
    print(data2.json())
except ValidationError as e:
    print(e.json())

print("*" * DELIMITER_SIZE)
orders = [mock.get_mocked_order() for i in range(2)]
orders[1]["email_address"] = "asd"
try:
    data2 = OrdersList(**{"list_name" : "Silpo", "orders" : orders})
    print(data2.json())
except ValidationError as e:
    print(e.json())
