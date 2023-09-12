"""Warm up classmethod  &  Staticmethod """

# A class method can access or modify the class state while 
# a static method can’t access or modify it.
# demonstrate static methods
  
# Python program to demonstrate use of a static method 
class Person: 
    def __init__(self, name: str, age: int): 
        self.name = name 
        self.age = age 
        
    # a static method to check if a Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
          
# Driver's code
if __name__ == "__main__":
    res = Person.isAdult(12)
    print('Is person adult:', res)
      
    res = Person.isAdult(22)
    print('\nIs person adult:', res)



# Python program to demonstrate use of a class method with static method 
from datetime import date
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
person1 = Person('Maximchik', 21)
person2 = Person.fromBirthYear('john', 1996)
 
print(person1.age)
print(person2.age)
print(person2.name)
 
# print the result
print(Person.isAdult(22))


# Is person adult: False

# Is person adult: True
# 21
# 27
# True