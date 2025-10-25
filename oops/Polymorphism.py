r"""

### Polymorphism

    method or symbol behaves in differently in different situation
    one name different forms(like different tasks)
    example:
         1+2 --> 3
        'a'+'b' --> ab 
        
    example:
        human behaviour
        
    example:
        ben 10 (many alien forms)
        transformer (optimus prime, bumbelebee)
        hulk
        VIP Dhanush vehicle
        
## Two Types :

    1) complie time Polymorphism

        - Method overloading
        - operator overloading

    2) Runtime Polymorphism

        - Method Overriding


### Complie Time Polymorphism

## operator overloading

# example:
print(10+1000)
print("10"+"1000")

# 1010
# 101000
# this is the best example for operator overloading

## Method overloading

# actually it won't raise error in java because it supports but in python method overloading is not possible because python run line by line execution
# but we can access indirectly variable length arguments (arbitary arguments)--> *args 

# example:

def add(a,b):
    print(a+b)
    
def add(a,b,c):
    print(a+b+c)
    
add(10,20,30) # 30 
# it skips the first function

add(10,20)
# Traceback (most recent call last):
#   File "C:\Users\VarunAakash\OneDrive\Desktop\Pyspyder_class\day18.py", line 54, in <module>
#     add(10,20)
# TypeError: add() missing 1 required positional argument: 'c'


### Runtime Ploymorphism

## method overriding 

class Remote:
    def turn_on(self):
        print('Take the remote first..')
    def options(self):
        print('Red Button')
class AC(Remote):
    def turn_on(self):
        print('Turn ON the AC..')
class TV(AC):
    def turn_on(self):
        print('Turn ON the TV..')
        
ac1 = AC()
ac1.turn_on()
ac1.options()
print(AC.mro())

# Turn ON the AC..
# [<class '__main__.AC'>, <class '__main__.Remote'>, <class 'object'>]


"""

