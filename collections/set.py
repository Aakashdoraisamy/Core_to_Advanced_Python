"""
## SET

Group of elements seperated by commas and enclosed by flag brackets

to create empty set use 
s1 = set()
print(s1)

set = {val,val2....valn}
s = {10,20,30,3,5,'Don'}
print(s) # {10,20,30,3,5,'Don'}
print(type(s)) # <class 'set'>
print(len(s)) # 3


# PROPERTIES OF SET

    - set can be homogeneous or heterogeneous
    - set are unordered collections
    - set won't allow duplicates won't raise error 
    example:
        s1 = {1,1,2,3,4,2}
        print(s1) # {1,2,3,4}
    - set supports unique elements only
    - set doesn't support indexing if by mistake we use indexing we get => error : 'set' object is not subscriable
    - set doesn't support slicing
    - set are mutable collection
    - set supports data types(int,float,boolean,string,complex,tuple) as elements 
    - other data types like list and inside tuple nested tuple dict won't allowed it raise error => Unhashable type : 'list'
     
# SET COMPRENSION

---> It is possible no need to use type casting like tuple
example:
s1 = {x for x in range(1,11)}
print(s1) # {1,2,3,4,5,6,7,8,9,10}

scenari0 1:
    s1 = {100 for x in range(1,11)}
    print(s1) # {100} --> ignores duplicates
    
example 2L
s1 = {int(input('enter your input:')) for x in range(1,11)}
print(s1)

# BUILD IN METHODS

1) ADD METHOD
s = {10,20,30,40,50}
s.add(60)
print(s) # {50,20,10,40,60,30} --> it add randomly places are shuffled

2) POP METHOD
s = {10,20,30,40,50}
s.pop()
print(s) # {20,10,40,60,30} 50 --> after randomly shuffled it removes first element which is randomly shuffles
# if set is empty it raise type error

3) REMOVE METHOD
s = {10,20,30,40,50}
s.remove(20)
print(s) # {50,40,10,30}
s.remove()
s.remove(100)--> if we didn't mention any value or out of value it --> raise 'key error'

4) DISCARD METHOD
s = {10,20,30,40,50}
s.discard(20)
print(s) # {50,40,10,30}
s.discard(100) --> it won't raise error it just skip it

    Difference Between Remove and Discard
        - Remove raise error when the value is not present in the set
        - Discard just skip it and returns others
        - it raise as key error not value because dict and set are belongs to one family everything consider as key value pairs so it will be key error
        
5) CLEAR METHOD
s = {10,20,30,40,50}
s.clear()
print(s) # it retuens empty set --> set() clears everything

6) COPY MEHTOD
s1 = {10,20,30,40,50}
s2 =s1.copy()
print(s1) # {50, 20, 40, 10, 30}
print(s2) # {50, 20, 40, 10, 30}
print(id(s1)) # 2726250700512
print(id(s2)) # 2726250701856

7) SUBSET METHOD

s1 = {1,2,3,4,5,6}
s2 = {3,4,5}
s3 = {10,3,4}
print(s2.issubset(s1)) # True
print(s3.issubset(s1)) # False

8) SUPERSET METHOD

s1 = {1,2,3,4,5,6}
s2 = {3,4,5}
s3 = {10,3,4}
print(s1.issuperset(s2)) # True
print(s1.issuperset(s3)) # False

9) INTERSECTION

s1 = {1,2,3,4,5,10,40}
s2 = {10,20,30,40,1,4}
print(s1.intersection(s2))

10) UNION

s1 = {1,2,3,4,5,10,40}
s2 = {10,20,30,40,1,4}
print(s1.union(s2))

11) DIFFERENCE

s1 = {1,2,3,4,5,10,40}
s2 = {10,20,30,40,1,4}
print(s1.difference(s2))

12) UPDATE

s1 = {1,2,3,4,5,10,40}
s2 = {10,20,30,40,1,4}
s1.update(s2)
print(s1) # instead of creating new set it will update any of sets as we given input sets it was for union

13) INTERSECTION_UPDATE

s1 = {1,2,3,4,5,10,40}
s2 = {10,20,30,40,1,4}
s1.intersection_update(s2)
print(s1) # instead of creating new set it will update any of sets as we given input sets it was for intersection

14) DIFFERENCE_UPDATE

s1 = {1,2,3,4,5,10,40}
s2 = {10,20,30,40,1,4}
s1.difference_update(s2)
print(s1)

15) SYMMETRIC_DIFFERENCE

s1 = {1,2,3,4,5,10,40}
s2 = {10,20,30,40,1,4}
s3 = s1.symmetric_difference(s2)
print(s3) # IT IGNORES COMMON VALUES

14) SYMMETRIC_DIFFERENCE_UPDATE

s1 = {1,2,3,4,5,10,40}
s2 = {10,20,30,40,1,4}
s1.symmetric_difference_update(s2)
print(s1) # IT IGNORES COMMON VALUES INSTEAD OF CREATING NEW SET IT STORES IN ANY OF SET

15) ISDISJOINT 

s1 = {1,2,3,4,5}
s2 = {10,20,30}
s3 = {10,20,4}
print(s1.isdisjoint(s2)) # TRUE
print(s1.isdisjoint(s3)) # FALSE


## WRITE A PROGRAM ADD WITHOUT USING BUILD IN METHOD

s = {1, 2, 3}
new = {int(input("Enter your value to add: "))}  # take input and make it a set
s = s | new   # use union instead of add() method 
print(s)


s = {i for i in range(1,21) if not i%2}
print(s)

    (or)
    
s = {i for i in range(1,21) if i%2 == 0}
print(s)

# SET WON'T SUPPORT RANGE


"""


# < ----------------------------------------- ########################### ------------------------------------>#

"""
# LIST CONCATIATION IS POSSIBLE BUT NOT WITH SET IS POSSIBLE
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
print(l3)
l4 = l1*4
print(l4)

# WHY SETS OR NOT CONCATING
    - Sets are unordered
    - Sets store only unique elements
    - Set operations are based on mathematics
    - They follow mathematical set theory for union, intersection, difference, etc.

l = [1,2,3,4,5]
for i in range(len(l)):
    print(i) --> returns index 0,1,2,3,4
    print(l[i]) --> returns 1,2,3,4,5

"""

# <------------------------------------------------- ############################ ------------------------------------> #



l = [1,2,3]
for i in range(len(l)):
    print(i) # 0,1,2 --> takes as inndex only
    
l = [1,2,3]
for i in range(len(l)):
    print(l[i]) # 1,2,3

