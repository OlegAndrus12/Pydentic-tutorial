import mock
from datetime import datetime
from collections import namedtuple
from typing import NamedTuple

# tuple is unmutable

class OrderNamedTuple(NamedTuple):
    order_id: int
    email_address: str
    checkout_date: datetime
    phone_number: str
    tags: List[str]


order = tuple(mock.get_mocked_order().values())

print(order[0]) # access by index is error-prone

tuple_class = namedtuple('NamedTupleDataClass', ['order_id', 'email_address', 'checkout_date', 'phone_number', 'tags'])
order2 = tuple_class(**mock.get_mocked_order())

print(order2.order_id)
print(order2[0])

order3 = OrderNamedTuple(**mock.get_mocked_order())
