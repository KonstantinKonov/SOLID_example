from orders import Order, PaymentProcessor

order = Order()
order.add_item('keyboard', 1, 50)
order.add_item('ssd', 1, 150)
order.add_item('usb cable', 2, 5)

print(order.total_price())
pay = PaymentProcessor()
pay.pay_debit(order, security_code='1234567')