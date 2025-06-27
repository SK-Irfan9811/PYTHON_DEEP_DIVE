class Payment:
    def pay(self):
        pass


class CreditCard(Payment):
    def pay(self):
        pass


class DebitCard(Payment):
    def pay(self):
        pass


class GiftCard(Payment):  # this violates the LSP as we can't pay though gift cards
    def pay(self):
        pass
