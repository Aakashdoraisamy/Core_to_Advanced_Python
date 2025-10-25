r"""

## it hides the implementation and provides the functionality to the user

Yes — in any normal Python function, when you call it, the print() outputs on the terminal. So from the user’s perspective, it looks similar whether you use abstraction or not.

The difference with abstraction is not what the user sees on the terminal — it’s how the code is structured and protected behind the scenes. Let me explain clearly:

🔹 Normal Function
def add(a, b):
    print("Adding numbers")
    return a + b

result = add(5, 3)
print(result)


Output:

Adding numbers
8

User can see the printed text and the result.

The function is directly callable.

Nothing is hiding — the user could also see the code if they open the file.

🔹 Using Abstraction
from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass  # No implementation yet (hidden)

class MyCalc(Calculator):
    def add(self, a, b):
        print("Adding numbers internally")
        return a + b

calc = MyCalc()
print(calc.add(5, 3))


Output:

Adding numbers internally
8


The user still sees the print and result, just like a normal function.

What’s hidden here:

The abstract class Calculator ensures that any subclass must implement add().

The internal rules of how addition is done (or in a more complex system, authentication, encryption, engine start, etc.) are not exposed to the user.

User cannot call Calculator.add() directly.

This provides structure, security, and flexibility that normal functions don’t provide.

    print statements will always show in terminal, but abstraction is not about hiding the output — 
    it’s about hiding the implementation, enforcing rules, and protecting sensitive logic behind 
    a clean interface.
    
    
| Aspect                    | Normal Function | Abstraction                                          |
| ------------------------- | --------------- | ---------------------------------------------------- |
| Call directly?            | ✅ Yes          | ❌ No, must implement in subclass                   |
| Internal logic exposed?   | Mostly yes      | Hidden behind abstract class / interface             |
| Enforces structure?       | No              | Yes — all subclasses must implement abstract methods |
| Protects sensitive steps? | No              | Yes, hides internal working from user                |

    
    example :
        Laptop


step 1 : -

from abc(module) import ABC(class),abstractmethod(method)

step 2 : -

creation of Abstraction class

step 3 : -

Inherit ABC class

step 4 : -

hide the implementation of abstractmethod(pay) by using @abstractmethod and pass

step 5 : -

create the concrete class

from abc import ABC, abstractmethod

#Abstraction class
class Payment(ABC):
    
    @abstractmethod
    def pay1(self):
        pass
    
# Concrete class

class UPI(Payment):
    def pay1(self):
        print('Welcome to UPI Payment....')

    def pay2(self):
        print('option 2 .....')

class NetBanking(Payment):
    def pay1(self):
        print('Welcome to UPI Payment....')
        
upi = UPI()
upi.pay1() # Welcome to UPI Payment.... 

# it works because we abstracted in abstract class but if we try to create different def function like

# Traceback (most recent call last):
#   File "C:\Users\VarunAakash\OneDrive\Desktop\Pyspyder_class\oops\abstraction.py", line 49, in <module>
#     upi = UPI()
#           ^^^^^
# TypeError: Can't instantiate abstract class UPI without an implementation for abstract method 'pay'

"""
 
class ethu_nagarjuna:
        
        scene = 'valthukal'
        
        def __init__(self):
                self.name = 'superstar'
                self.jr = 'mohan'
                self.movie = 'coolie'
                
        def dhanunjay(self):
                print(self.jr)
                print(self.scene)
                
e = ethu_nagarjuna()
e.dhanunjay()