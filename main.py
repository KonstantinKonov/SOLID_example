from orders import Order, PaymentProcessor, DebitPaymentProcessor, PaypalPaymentProcessor

order = Order()
order.add_item('keyboard', 1, 50)
order.add_item('ssd', 1, 150)
order.add_item('usb cable', 2, 5)

print(order.total_price())
pay = DebitPaymentProcessor(security_code='1234567')
pay.pay(order)

pay_by_paypal = PaypalPaymentProcessor(email='something@something.com')
pay_by_paypal.pay(order)


# LSP - можно заменить родительским методом 
def make_payment(order, payment_method: PaymentProcessor):
    payment_method.pay(order)
make_payment(order, PaymentProcessor())