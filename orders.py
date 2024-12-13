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


class PaymentProcessor:
    def pay_debit(self, order: Order, security_code):
        print('processing debit payment type')
        print(f'verifying security code: {security_code}')
        order.status = 'paid'

    def pay_credit(self, order: Order, security_code):
        print('processing credit payment type')
        print(f'verifying security code: {security_code}')
        order.status = 'paid'