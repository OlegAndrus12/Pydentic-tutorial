import mock
from datetime import datetime
from typing import List

class OrderPlainDataClass():
    
    def __init__(self, order_id: int, email_address: str, checkout_date: datetime,
                phone_number: str, tags: List[str]):
        
        self.order_id = order_id
        self.email_address = email_address
        self.checkout_date = checkout_date
        self.phone_number = phone_number
        self.tags = tags

order = OrderPlainDataClass(**mock.get_mocked_order())

