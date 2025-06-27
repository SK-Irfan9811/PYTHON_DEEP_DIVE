# low level module
class CreditCard:
    def pay(self):
        print("Paying with credit card")


# high level module
class PaymentProcessor:
    def pay(self):
        c = CreditCard()
        c.pay()


# violates the DIP as high level module is dependent on low level module
p = PaymentProcessor()
p.pay()


# solution - both should depend on abstraction
# abstraction
class PaymentMethod:
    def pay(self, amount):
        pass


# low level modules
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} with credit card")


class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} with debit card")


# high level module
class PaymentProcessor:
    def __init__(self, method: PaymentMethod):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)


p = PaymentProcessor(CreditCard())
p.process(100)
