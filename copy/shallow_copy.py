# Definition:
# A shallow copy creates a new container (like a list or dictionary), but the elements inside it are the same objects as in the original.

# Outer object → new memory address

# Inner elements → same memory addresses


# l = [[100,150,250,350],[10,15,25,35]]
# l1 = l.copy()
# # it creates new copy it stores new address
# print(id(l)) # 2521297197376  # Outer list address
# print(id(l1)) # 2521297195392 # # Different outer list address

# # here the values pointing same address because it is inside the collection
# print(id(l[0])) # 140723914151448
# print(id(l1[0])) # 140723914151448

# # l1[0] = 1000
# # print(l1) # [1000, 150, 250, 350]
# # print(l)  # [100, 150, 250, 350]

# l[0][1] = 1000
# print(l)
# print(l1)
# print(id(l)) # 2579001701184
# print(id(l1)) # 2578999061824

# # same because it was not copy we just assigning

# l = [100,150,250,350]
# l1 = l
# print(id(l)) # 2626216129344
# print(id(l1)) # 2626216129344

# l1[1] = 100
# print(l) # [100, 100, 250, 350]
# print(l1) # [100, 100, 250, 350]
# print(id(l1)) # 1419693988160
# print(id(l))  # 1419693988160

import copy
l = [[100,150,250,350],[10,15,25,35]]
l1 = copy.copy(l)

print(id(l))  # 3104956093376
print(id(l1))  # 3104955740416

print(id(l[0])) # 3104952816000
print(id(l1[0]))  # 3104952816000

l[0][1] = 1000
print(l)
print(l1)
print(id(l)) 
print(id(l1)) 

# [[100, 1000, 250, 350], [10, 15, 25, 35]]
# [[100, 1000, 250, 350], [10, 15, 25, 35]]
# 3104956093376
# 3104955740416