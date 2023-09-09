"""factory method to resolve the payment method here """

class Payment:
# __new__ is a static method that's responsible for creating and 
# returning a new instance of the class. 
    def __new__(cls, payment_type: str ) :
        if payment_type == "paypal":
            return object.__new__(PaypalPayment)
        elif payment_type == "card":
            return object.__new__(StripePayment)


class PaypalPayment(Payment):
    def pay(self, amount: int)->None:
        print(f"Paying :{amount} Using Paypal") 

class StripePayment(Payment):
    def pay(self, amount: int)->None:
        print(f"Paying :{amount} Using Stripe") 




def main() -> None:
    my_payement = Payment("card")
    if my_payement:
        my_payement.pay(450)
    else:
        print("You Have not chosen the correct Option ")
    
if __name__ == "__main__":
    main()

# OutPut:
# Paying :450 Using Stripe