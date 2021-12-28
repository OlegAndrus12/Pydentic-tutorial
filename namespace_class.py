import mock
from types import SimpleNamespace

order = SimpleNamespace(**mock.get_mocked_order())

print(order.order_id)