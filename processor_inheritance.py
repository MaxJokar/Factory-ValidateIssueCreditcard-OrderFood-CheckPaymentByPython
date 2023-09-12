"""
Classmethod to implement instead of  depenancy-injection 
we can update/modify daily prices for our product provided in our Burgershop
using a list of product propertionally with their price as a list 
"""
from processor_dep_injection import PRICES


class OrderPaymentHandler:

    PRICES ={
        'salad' : 20_52,
        'drink':15_38,
        'fish':50_55 ,
        'burger':85_55 ,
        'sausage':74_55 ,
    }
    
    def __init__ (self, items: list[str],PRICES ):
        self.items = items
        self.PRICE = PRICES
        # print("this is init part test:",self.PRICES)

    def calculate(self, items , PRICES):
            total = sum(PRICES[item] for item in items)
            print(f"Your order for {items} is : {total/100:.2f}")    
            print(f"BYE BYE ")
        

    @classmethod
    def  order_food(cls, items: list[str] , PRICES) : 
        
        
            total = sum(PRICES[item] for item in items)
            print(f"\n\Classmethod: Your order for {items} is : {total/100:.2f}")
            # print(f"your order is : {total/100:.2f}")
            # we dont have here @staticmethod or @classmethod 
            
            print(" Thanks for shopping  \n")
            
    

def main():
    order1 = OrderPaymentHandler(["drink","sausage"],PRICES )
    # print("heeeeeeeelooooooooooo",order1.items)
    print("this is order1partOneTest")
    order1.calculate(["drink","sausage"],PRICES )   
    OrderPaymentHandler.order_food(["drink","salad"] ,OrderPaymentHandler.PRICES )

if __name__ == "__main__":
    main()


# Output:
# your order for ['drink', 'salad'] is : 35.90
# charging from Your card  :35.90
# thanks for shopping