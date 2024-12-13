from orders import Order, DebitPaymentProcessor

order = Order()
order.add_item('keyboard', 1, 50)
order.add_item('ssd', 1, 150)
order.add_item('usb cable', 2, 5)

print(order.total_price())
pay = DebitPaymentProcessor()
pay.pay(order, security_code='1234567')