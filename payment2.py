"""A simpler & straighforward way compared with payment1 """
from enum import Enum
from typing import Protocol

class PayementMethod(Enum):
    PAYPAL = "paypal"
    CARD = "card"


class Payment(Protocol):
    def pay(self, amount: int)->None:
        pass
    
    
class PaypalPayment(Payment):
    def pay(self, amount: int)->None:
        print(f"Paying :{amount} Using Paypal") 

class StripePayment(Payment):
    def pay(self, amount: int)->None:
        print(f"Paying :{amount} Using Stripe") 


#  instead of using __new__in payment1 we can use the dictionary following :
PAYMENT_METHODS:dict[PayementMethod , type[Payment]] = {
    PayementMethod.CARD: StripePayment,
    PayementMethod.PAYPAL: PaypalPayment,
}




def main():
    my_payement = PAYMENT_METHODS[PayementMethod.PAYPAL]()
    my_payement.pay(250)
    
if __name__ == "__main__":
    main()

# OutPut:
# Paying :250 Using Paypal