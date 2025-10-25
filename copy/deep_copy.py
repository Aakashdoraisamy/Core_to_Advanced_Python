# Deep Copy (Python)

# A deep copy creates a new object and recursively copies all objects nested inside it.

# The copy is completely independent of the original.

# Modifying the deep copy does not affect the original object, even for nested/mutable elements.

# In Python, use the copy.deepcopy() function from the copy module.


import copy

s = [1,2,[1,10,11,5]]
s1 = copy.deepcopy(s)

print(id(s)) # 2607908854080
print(id(s1)) # 2607912129600

print(id(s[0])) # 140723920243128
print(id(s1[0])) # 140723920243128

s[0] = 100
print(s) # [100, 2, [1, 10, 11, 5]]
print(s1) # [1, 2, [1, 10, 11, 5]]

s[2][0] = 100

print(s) # [100, 2, [100, 10, 11, 5]]
print(s1)  # [1, 2, [1, 10, 11, 5]]

print(id(s))
print(id(s1))

# | Copy Type    | Outer List Address | Inner Lists Address |
# | ------------ | ------------------ | ------------------- |
# | Shallow Copy | New                | Same as original    |
# | Deep Copy    | New                | New copies          |

