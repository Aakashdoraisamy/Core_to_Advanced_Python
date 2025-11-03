r"""

## Encapsulation
    - Binding data members(atributes) and methods together in a single unit with the help of (private, public, protected)
    - private can access by using getter and setter methods
    - Public: can be accessed from anywhere
    - Private: can be accessed only within the class
    - Protected: can be accessed within the class and its subclasses    
    - Getter and Setter: methods to access and modify private attributes
    - Decorators: special methods to modify the behavior of getter and setter methods


class user:
    
    def __init__(self):
        self.u_name = input('Enter Your Name:')
        self.u_id = input('Enter Your ID:')
        self.u_mobile_number = input('Enter Your Mobile Number:')
        self.follower_count = 0
        self.following_count = 0
        
    def display_details(self):
        print("User Details:")
        print(f"Name: {self.u_name} ID: {self.u_id} Mobile Number: {self.u_mobile_number} Followers: {self.follower_count} Following: {self.following_count}")


print('USER 1 DETAILS:')
u1 = user()
u1.display_details()

print('USER 2 DETAILS:')
u2 = user()
u2.display_details()

## Access Specifiers

# public variable and method accessing

class Instagram:
    name = 'Instagram'
    
    def __init__(self):
        self.u_name = input('Enter your Name:')
        self.u_id = input('Enter Your ID:')
        self.u_mobile = int(input('Enter Your Mobile Number:'))
        self.following = 0
        self.followers = 0
    def display(self):
        print(f'Name : {self.u_name}\nFollowers : {self.followers}\nFollowing : {self.following}')
        print(f'Mobile Number : {self.u_mobile}') # accesing public variable
    def check(self):
        self.u_name = 'ABC' # updation is possible inside the class
        self.display() # accessing Public method
        
user1 = Instagram()
user1.u_name = 'XYZ' # updation is possible outside the class but need to mention the display method not check
user1.display()
user1.check()

# protected variable and method accessing

Syntax : _var
         _protectedmethod()
        
protected can access only inside child class
        
class Instagram:
    name = 'Instagram'
    
    def __init__(self):
        self.u_name = input('Enter your Name:')
        self.u_id = input('Enter Your ID:')
        self._u_mobile = int(input('Enter Your Mobile Number:')) # protected variable
        self.following = 0
        self.followers = 0
    def display(self):
        print(f'Name : {self.u_name}\nFollowers : {self.followers}\nFollowing : {self.following}')
        print(f'Name : {self._u_mobile}') # accessing protected variable inside class recommended
    def check(self):
        self.u_name = 'ABC' # updation is possible inside the class
        self.display()
    def _check(self):
        pass
        
user1 = Instagram()
print(user1._u_mobile) # possible to access outside but not recommended
user1.u_name = 'XYZ' # updation is possible outside the class but need to mention the display method not check
user1.display()
user1.check()


Acess protected method inside and outside class and protected variable also

# --> accessing outside protected method and class is possible but not recommended 

class Instagram:
    name = 'Instagram'
    
    def __init__(self):
        self.u_name = input('Enter your Name:')
        self.u_id = input('Enter Your ID:')
        self._u_mobile = int(input('Enter Your Mobile Number:'))
        self.following = 0
        self.followers = 0
    def _display(self):
        print(f'Name : {self.u_name}\nFollowers : {self.followers}\nFollowing : {self.following}')
        print(f'Mobile Number: {self._u_mobile}')
    def check(self):
        self.u_name = 'ABC' # updation is possible inside the class
        # self._u_mobile = 9876543210 # accessing protected variable inside class possible (but not recommended)
        self._display() # accessing Protected inside class
        
user1 = Instagram()
user1._u_mobile = 9976287350 # accessing protected variable outside class (but not recommended)
# user1._display() # access outside class
user1.check() 

# Private Variable and Method Accessing :

syntax : __var
        __method()
        
accessing outside is not possible

class Snapchat:
    name = 'Snapchat'
    def __init__(self):
        self.__streaks = 150
    def __display(self):
        print(self.__streaks) 
        print(f"Current Streak : {self.__streaks}")
    def dis(self):
        # print(self.__streaks) # private method is possible to access inside the class
        print(f'Class Name : {self.name}')
        self.__streaks = 200 # updation inside the class possible
        self.__display() # accessing private method inside the class

user1 = Snapchat()
# user1.__display() # private method not able to access outside the class
# print(user1.__streaks) # private variable is not able access outside the class
# user1.__streaks = 300 # it won't raise error and won't update because it breaks the rule so it acts as like public variable and updation
# print(user1.__streaks)
user1.dis()

## Encapsulation : 

Encapsulation is an object-oriented programming concept that combines data (attributes) and methods into a single unit (class), restricting direct access to some components to protect the internal state.

Private members (e.g., __var) cannot be accessed directly outside the class.
Public members (e.g., var) can be accessed from anywhere.
Getter and setter methods are used to access and modify private attributes, providing controlled and secure access.
Encapsulation ensures data security, hides implementation details, and allows changes without affecting external code.

# getter and setter

class Person:
    def __init__(self, name):
        self.__name = name  # private variable

    def get_name(self):     # getter
        return self.__name

    def set_name(self, name):  # setter
        self.__name = name

p = Person("Alice")
print(p.get_name())    # Output: Alice
p.set_name("Bob")
print(p.get_name())    # Output: Bob

class Linkedin:
    
    def __init__(self):
        self.__connections = 2000
    def getter(self):
        print(self.__connections)
    def setter(self,c):
        self.__connections = c

user1 = Linkedin()
user1.getter()
user1.setter(5000)
user1.getter() # updation is possible through getter and setter outside the class to access the private variable and method

"""