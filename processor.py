"""
A simple but Powerful script to prove the imporatnce of :Depenancy injection
which is a Powerful mechanism for connecting things 
for OOP in Python instead of inharitance, here is an example
"""
class StripPaymentHandler:
    def handle_payment(self, amount:int)-> None:
        print(f"charging from Your card  :{amount/100:.2f} ")

PRICES ={
    'salad' : 20_52,
    'drink':15_38,
    'fish':50_55  
}


# instead of inheritance we can use this method to access the class!
def  order_foot(items: list[str] ,payment_handler: StripPaymentHandler)-> None:
    total = sum(PRICES[item] for item in items)
    print(f"your order is : {total/100:.2f}")
    payment_handler.handle_payment(total)
    print("thanks for shopping  \n")
    
    




def main():
    order_foot(["drink","salad"] , StripPaymentHandler())

if __name__ == "__main__":
    main()


# Output:
# your order is : 35.90
# charging from Your card  :35.90
# thanks for shopping
    