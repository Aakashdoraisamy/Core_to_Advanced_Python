"""
## TUPLE

BUILD IN METHODS

1.count

t1 = (10,20,30,40,50,60,10,70)
print(t1.count(10) # 2

2. index

t1 = (10,20,30,40,50,60,10,70)
print(t1.index(10)) #0
print(t1.index(10,1)) # 6
print(t1.index(10,2,6)) # value error

# t = int(input('Enter Your range:'))
# l = (i for i in range(1,t+1) if i%2==0)
# print(tuple(l))

## TUPLE COMPRENSION

IT IS NOT POSSIBLE TECHINCALLY WE CAN GET OUTPUT OF GENERATOR OBJECT AS OUTPUT BUT WE CAN GET BY THROUGH TYPE CASTING

t = tuple(i for i in range(10))
print(t)

-----> TUPLE IS IMMUTABLE <------

but we can update it by inside mention as list

t = (0,[1,2,3])
t[1][2] = 1000
print(t) # (0,[1,2,1000])

tuple can supports concatation because updation and deletion was not support directly but 

t = (1,2,3) + (4,5,6)
print(t) # it creates new tuple not creating extisting so it is possible by this way
# (1,2,3,4,5,6)

"""

