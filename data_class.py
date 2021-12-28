import mock
from datetime import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class OrderDataClass:    
    
    order_id: int
    email_address: str
    checkout_date: datetime
    phone_number: str
    tags: List[str]

order = OrderDataClass(**mock.get_mocked_order())