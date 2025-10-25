r"""
### OOPS concept: Class and Objects

                class 
                  |
                  | (attribute)
                  |
      ---------------------------
      |                         |
      |                         |
  (variables)                (methods)
        |                       |    
        |                       |    
  ---------------         ---------------------------------------
  |             |         |            |            |           |
(instance)   (class)    (instance)    (class)    (static)     (magic)

"""

# ---------------------------------- #################################### ---------------------------- #

r"""
# class pyspyder:
#     print('hello')
# print(dir(pyspyder))
# print(len(dir(pyspyder))) # 27 python version 3.12.6
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

## Class Variables

class car:
    wheels = 4
    print(wheels)
c = car()

## Instance Variables

# self stores the address of the object when it stores if we create instance variable
# only self can access the instance variable without throwing error if we try to access like b = bike() it won't raise error it internally stores address of the object

class bike:
    def __init__(self):  # ---> __init__ is a constructor which is used to initialize the instance variable by deafult if we pass without calling function it will exec
        self.name = 'GT650'
        self.color = 'RED'
        self.price = 400000
        # print(self) # it will print address of the object <__main__.bike object at 0x000002968CAB6C90>
        
# outside the class we can access both instance and class variable
b = bike() # by default it pass address of the object of all instance variable
# b1 = bike() <__main__.bike object at 0x000001AE5238E3C0>
# b is an object of bike class 
# address will differ while we create multiple objects
# print(dir(b)) # it will print all the attributes of the object
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'name']
print(b.name)
print(b.color)
print(b.price)

class game:
    def __init__(self, name, type, players):
        self.name = name
        self.type = type
        self.players = players
        print(self) # it will print address of the object <__main__.game object at 0x000002968CAB6C90>
cricket = game('Cricket', 'Outdoor', 11)
print(cricket.name)
print(cricket.type)
print(cricket.players)
football = game('Football', 'Outdoor', 11)
print(football.name)
print(football.type)
print(football.players)

# output:
# <__main__.game object at 0x0000023752D5E840>
# Cricket
# Outdoor
# 11
# <__main__.game object at 0x0000023752D5E870>
# Football
# Outdoor
# 11


class game:
    def __init__(self, name, type, players):
        self.name = name
        self.type = type
        self.players = players
        print(self) # it will print address of the object <__main__.game object at 0x000002968CAB6C90>
        
    def details(self): # --> it won't raise error but it won't print anything because we didn't create object of the class
        print('------------------')
        print(f'Name: {self.name}')
        print(f'Type: {self.type}')
        print(f'Players: {self.players}')
        print('------------------')
        print('this is details of cricket') 
        
cricket = game('Cricket', 'Outdoor', 11)
print(cricket.name)
print(cricket.type)
print(cricket.players)
cricket.details() 

# if we directly call the method without creating object of the class it will throw error like
# Traceback (most recent call last):
#   File "C:\Users\VarunAakash\OneDrive\Desktop\pyspyder class\day15.py", line 99, in <module>
#     cricket.details() 
#     ^^^^^^^^^^^^^^^^^
# TypeError: game.details() takes 0 positional arguments but 1 was given

# which means it is expecting 0 arguments but 1 is given because when we create object of the class it automatically pass address of the object to the first argument which is self so it is expecting 0 arguments but 1 is given


"""

# ---------------------------------- #################################### ---------------------------- #

r"""
## 4 Pillars of OOPS
   - Abstraction
   - Encapsulation
    - Inheritance
    - Polymorphism
    
## Encapsulation
    - Binding data members(atributes) and methods together in a single unit with the help of (private, public, protected)
    - private can access by using getter and setter methods
    - Public: can be accessed from anywhere
    - Private: can be accessed only within the class
    - Protected: can be accessed within the class and its subclasses    
    - Getter and Setter: methods to access and modify private attributes
    - Decorators: special methods to modify the behavior of getter and setter methods

"""
r"""
# scenario:
    # 1) create a user
    #  u_name(input from the user)
    #  u_id(input from the user)
    #  u_mobile_number(input from the user)
    #  follower count(assign 0)
    #  following count(assign 0)
    
    #  2) display the user details
    #  3) create 2 user
    
"""

r"""

### staticmethod
    - it is a method in class which is not having a self and cls data 
    - static method is normal function 
    - static method doesn't have self variable to store the address
    - it is basically acts like normal function but when we want to use inside class normal calculations for that we can't use instance or classmethod that's why staticmethod we use not only calculatuions normal calling function
    
## syntax:

class Name:
    @staticmethod
    def functionname():
        statement       ---> acts as normal function and not possible to access class and instance method it is user defined function
   
    
class ABC:
    
    @staticmethod
    def add(a, b):
        return a + b
    
    def fun(self, a, b):
        result = ABC.add(a, b) 
        print(f'{result} is Result of sum')

obj = ABC()
obj.fun(2, 3)

"""

r"""

### classmethod

class method is the property of class and it can access only class variable and variable and it's not possible to access instance variable


class P_H:
    value = 8
    def fun(self):
        self.new = 'hello'
        print(self)
    @classmethod
    def new_class(add):
        print(add.value)
        # print(add.new) # not possible to access instance variable or method
        print(P_H) # <class '__main__.P_H'> ---> address for both are same because it indicates class
        print(add) # <class '__main__.P_H'>
        
obj = P_H()
obj.fun()
obj.new_class()
print(obj.new)

"""
