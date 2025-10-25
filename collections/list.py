"""
COLLECTIONS

    - lIST
    - TUPLE
    - SET
    - DICTIONARY
    
    
### List
    
list()
list_1 = [val1,val2,val3,...]

Properties of list:
    - List is both Homogeneous(same) and Heterogeneous(different) data type
    - ordered collection of items
    - can store duplicate values 
    - List suppprts indexing and slicing (both positive and negative)
        - to access a value from a list we have two scenarios
            - to get a value from a list
            - to update a value in a list     
    - Group of values are seperated by comma and enclosed within []
    - can store different data types
    - list are mutable
 
 
    
l1 = list(input("Enter multiple values: "))
print(l1,type(l1))

Enter multiple values: [1,2,3,4,5]
['[', '1', ',', '2', ',', '3', ',', '4', ',', '5', ']'] <class 'list'>

# taking everything as string or characters including the braces and commas

Enter multiple values: 1,2,3,45
['1', ',', '2', ',', '3', ',', '4', '5'] <class 'list'>

to avoid this we can use eval() function

l1 = eval(input("Enter multiple values: "))
print(l1,type(l1))

Enter multiple values: [1,2,3,4,5]
[1, 2, 3, 4, 5] <class 'list'>

Enter multiple values: 1,2,3,4,5
(1, 2, 3, 4, 5) <class 'tuple'>

l = [1,2,3,4,5]
l[100] = 100
    (or)
l[-100] = 100
print(l[2],l)
IndexError: list assignment index out of range


l = ["Hello","Hi",1,2,100,4,46,78]
print(l[1:5]) # ['Hi', 1, 2, 100]
print(l[-7:-3]) # ['Hi', 1, 2, 100]
print(l[-7:-3:-1]) # [] because step is negative 
print(l[::2]) # ['Hello', 1, 100, 46]
print(l[::-1]) # [78, 46, 4, 100, 2, 1, 'Hi', 'Hello']

l = ["Hello","Hi",1,2,100,4,46,78]
print('before Indexing:',l)
l[0] = 25
l[1] = 1000
l[2] = 5000
l[3] = 'BYE'
print('After Indexing:',l)

# 2nd way to update a value in a list is by using slicing

l = ["Hello","Hi",1,2,100,4,46,78]
print('before Slicing:',l)
l[0:5] = [25,1000,5000,'BYE']
print('After Slicing:',l)

l = [12,24,36,58,69]
l += [100,200]
print(l) #[12, 24, 36, 58, 69, 100, 200]

l = [12,24,36,58,69]
del l[2]
print(l) #[12, 24, 58, 69]

l = ["Hello","Hi",1,2,100,4,46,78]
l[0:5] = [25,1000,5000,'BYE']
del l
print(l) # NameError: name 'l' is not defined

l = ["Hello","Hi",1,2,100,4,46,78]
l[0:5] = [25,1000,5000,'BYE']
del l[1]
print(l) # [25, 5000, 'BYE', 4, 46, 78]

# BUILD IN METHODS OF LIST => 11 Build in methods

# COPY METHOD

l = [1,2,3,10,50]
copy_list = l.copy()
print(copy_list,id(copy_list))
print(l,id(l))
copy_list[0] = 100
print(copy_list,l)
print(id(copy_list),id(l)) # both id are different because copy() creates a new list it is shallow copy

# CLEAR METHOD

l = [1,2,3,10,50]
res = l.clear()
print(res,l) # None []

l = [1,2,3,10,50]
l.clear()
print(l) # []

# APPEND METHOD

l = [1,2,3,10,50]
l.append(100)
print(l) # [1, 2, 3, 10, 50, 100]

l = [1,2,3,10,50]
l.append([10,20,30,40,50])
print(l) # [1, 2, 3, 10, 50, [10, 20, 30, 40, 50]]  # it appends the entire list as a single element

l = [1,2,3,4]
l.append([10,20,30,40,50])
print(l[4][4]) # 50 it accesses the 4th index element of the appended list 
print(l)

# INSERT METHOD

l = [1,2,3,10,50]
l.insert(2,100)
print(l) # [1, 2, 100, 3, 10, 50] it inserts the value at the specified index and shifts the rest of the elements to right

l = [1,2,3,10,50]
l.insert(10,100)
print(l) # [1, 2, 3, 10, 50, 100] it appends the value at the end if the index is greater than the length of the list

l = [1,2,3,10,50]
l.insert(-10,100)
print(l) # [100, 1, 2, 3, 10, 50] it inserts the value at the start if the negative index is greater than the length of the list

# EXTEND METHOD

l = [1,2,3,10,50]
l.extend([100,200,300])
print(l) # [1, 2, 3, 10, 50, 100, 200, 300] it extends the list by adding elements of the iterable (list, tuple, set, string, dictionary) to the end of the list

l = [1,2,3,4]
l.extend(100) # TypeError: 'int' object is not iterable

extends by appending elements from the iterable

Differnce between append() and extend()
- append() adds its argument as a single element to the end of a list. The length of the list itself will increase by one.
- extend() iterates over its argument adding each element to the list, extending the list.
l = [1,2,3]
l.append([4,5])
print(l) # [1, 2, 3, [4, 5]]

l = [1,2,3]
l.extend([4,5])
print(l) # [1, 2, 3, 4, 5]

# INDEX METHOD

l = [10,20,30,40,50,60,70,80,90,100]
print(l.index(50)) # 4 it returns the index of the first occurrence of the specified value

l = [10,20,30,40,50,60,70,80,90,100]
print(l.index(500)) # ValueError: 500 is not in list

# REMOVE METHOD

l = [10,20,30,40,50,60,70,80,90,100]
l.remove(50)
print(l) # [10, 20, 30, 40, 60, 70, 80, 90, 100] it removes the first occurrence of the specified value

l = [10,20,30,40,50,60,70,80,90,100]
l.remove(500) # ValueError: list.remove(x): x not in list

# POP METHOD

l = [10,20,30,40,50,60,70,80,90,100]
print(l.pop()) # 100 it removes and returns the last item if index is not specified
print(l) # [10, 20, 30, 40, 50, 60, 70, 80, 90]

dIFFERENCE BETWEEN DEL AND POP METHOD
- del can be used to delete an item at a specific index or a slice of items, or even the entire list itself.
- pop() removes and returns an item at a specific index (default is the last item).

WHAT IS THE DIFFERENCE BETWEEN REMOVE() AND POP() METHOD AND DEL KEYWORD?
- remove() removes the first occurrence of a specified value from the list.
- pop() removes and returns an item at a specific index (default is the last item).
- del can be used to delete an item at a specific index or a slice of items, or even the entire list itself.

# COUNT METHOD

l = [10,20,30,40,50,60,70,80,90,100,10,20,10]
print(l.count(10)) # 3 it returns the number of occurrences of the specified value
print(l.count(500)) # 0 it returns 0 if the value is not found in the list

# REVERSE METHOD

l = [10,20,30,40,50,60,70,80,90,100]
l.reverse()
print(l) # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] it reverses the order of the list

# SORT METHOD

l = [10,20,30,40,50,60,70,80,90,100,1,5,3,7,9]
l.sort()
print(l) # [1, 3, 5, 7, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] it sorts the list in ascending order

L = ['banana', 'apple', 'orange', 'kiwi', 'grape']
L.sort()
print(L) # ['apple', 'banana', 'grape', 'kiwi', 'orange'] it sorts the list in ascending order alphabetically

"""

