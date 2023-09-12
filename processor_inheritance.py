"""
Classmethod to implement instead of  depenancy-injection 
"""
class StripPaymentHandler:

    PRICES ={
        'salad' : 20_52,
        'drink':15_38,
        'fish':50_55 ,
        'burger':85_55 ,
        'sausage':74_55 ,
    }
    
    def handle_payment(self, items: list[str] , PRICES):
        self.items = items
        self.PRICE = PRICES

       
        

    @classmethod
    def  order_foot(cls, items: list[str] , PRICES) : 
        
        
            total = sum(PRICES[item] for item in items)
            print(f"your order for {items} is : {total/100:.2f}")
            # print(f"your order is : {total/100:.2f}")
            # we dont have here @staticmethod or @classmethod 
            
            print("thanks for shopping  \n")
            
    

def main():
    StripPaymentHandler.order_foot(["drink","salad"] ,StripPaymentHandler.PRICES )

if __name__ == "__main__":
    main()


# Output:
# your order for ['drink', 'salad'] is : 35.90
# charging from Your card  :35.90
# thanks for shopping