# CHECKS IF TWO VARIABLES POINT TO THE SAME OBJECT IN MEMORY

a = int(input('Enter First Number:'))
b = int(input('Enter Second Number:'))
if id(a) == id(b):
    print('Both of Adrress are same')
else:
    print('Both are Not same')
    
    
# Possible Ways:

# Using is Operator (Recommended for identity check)

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a is b:   # checks if both point to same object
    print("Both point to the same object")
else:
    print("They are different objects")


# Using == Operator (Value Equality, not memory)

if a == b:
    print("Both have the same value")
else:
    print("Different values")


# Manual Address Comparison with ctypes

import ctypes

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if ctypes.addressof(ctypes.py_object(a)) == ctypes.addressof(ctypes.py_object(b)):
    print("Both objects share the same memory address")
else:
    print("Different memory addresses")


# Check Identity Using hash(id(x))

if hash(id(a)) == hash(id(b)):
    print("Both are same objects")
else:
    print("Not the same")
