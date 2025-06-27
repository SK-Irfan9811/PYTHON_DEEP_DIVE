# without OCP
class Payment:

    def pay(self, type_):
        if type_ == "UPI":
            print("payment done through UPI")
        elif type_ == "Card":
            print("Payment done through card")


p = Payment()
p.pay("UPI")


# with OCP
class Payment:
    def pay(self):
        pass


class CreditCardPayment(Payment):
    def pay(self):
        print("Payment done thorough credit card")

c=CreditCardPayment()
c.pay()
