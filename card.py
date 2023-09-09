from dataclasses import dataclass


# @dataclass
#  a data class is a class that is designed to only hold data values
# They are typically used to store information that will be passed between
# different parts of a program or a system.
@dataclass
class CreditCard:
    number:str
    expiry_month: int
    expiry_year: int
    

# instead of below we can do above using @dataclass
# class Person():
# def __init__(self, name, age, height, email):
#     self.name = name
#     self.age = age
#     self.height = height
#     self.email = email


# To Be Continued,....