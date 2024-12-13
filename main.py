from orders import Order, DebitPaymentProcessor, CreditPaymentProcessor, PaypalPaymentProcessor, SMSAuth, NotARobot

order = Order()
order.add_item('keyboard', 1, 50)
order.add_item('ssd', 1, 150)
order.add_item('usb cable', 2, 5)

print(order.total_price())

sms_auth = SMSAuth()
not_a_robot_auth = NotARobot()

debit_pay = DebitPaymentProcessor(security_code='1234567', authorizer=sms_auth)
debit_pay.authorizer.verify_code(code='9876')
debit_pay.pay(order)

credit_pay = CreditPaymentProcessor(security_code='1234567')
credit_pay.pay(order)

paypal_pay = PaypalPaymentProcessor(email='something@something.com', authorizer=not_a_robot_auth)
paypal_pay.authorizer.not_a_robot()
paypal_pay.pay(order)