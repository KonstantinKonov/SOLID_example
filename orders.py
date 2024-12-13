from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class PaymentProcessorSms(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass


class Authorizer:
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):
    authorized = False 

    def verify_code(self, code):
        print(f'verifying code {code}')
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def auth_sms(self, code):
        print(f'verifying sms code {code}')
        self.verified = True

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception('not authorized')
        print('processing debit payment type')
        print(f'verifying security code: {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order: Order):
        print('processing debit payment type')
        print(f'verifying security code: {self.security_code}')
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessorSms):
    def __init__(self, email, authorizer: Authorizer):
        self.email = email  
        self.authorizer = authorizer

    def auth_sms(self, code):
        print(f'verifying sms code {code}')
        self.verified = True

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception('not authorized')
        print('processing paypal payment type')
        print(f'verifying email address: {self.email}')
        order.status = 'paid'