import mock
import attr
from datetime import datetime
from typing import List

@attr.define
class OrderAttrClass:    
    
    order_id: int
    email_address: str
    checkout_date: datetime
    phone_number: str
    tags: List[str]

order = OrderAttrClass(**mock.get_mocked_order())
