import random
from faker import Faker

def get_mocked_order():
    fake = Faker()
    mock = {
        "order_id" : random.randint(0, 100),
        "email_address" : fake.email(),
        "checkout_date" : fake.date(pattern = "%Y-%m-%d"),
        "phone_number" : fake.phone_number(),
        "tags" : fake.words(),
    }
    print(mock)
    return mock