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


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order: Order):
        print('processing debit payment type')
        print(f'verifying security code: {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order: Order):
        print('processing credit payment type')
        print(f'verifying security code: {self.security_code}')
        order.status = 'paid'

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email  

    def pay(self, order: Order):
        print('processing paypal payment type')
        print(f'verifying email address: {self.email}')
        order.status = 'paid'