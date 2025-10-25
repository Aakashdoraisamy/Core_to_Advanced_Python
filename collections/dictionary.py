"""
# DICTIONARY
    - group of key value pairs seperated by commas and enclosed by {}
    - indside set if we pass continus number it returns ordered numbers
    
    # PROPERTIES OF DICT
        - ordered collection
        - both Homogeneous and Heterogeneous
        - it doesn't support indexing and slicing
        - key's can be immutable datatypes either string or tuple {'name':value} or {(1,2):value} (int,float,complex,complex wont support for key)
        - values can be any datatype
        - key should be unique(should not be duplicate) but values can be duplicate
        - dictionary is mutable collection
        
        
d = {1:100,2:100,4:550,1:150}
print(d)
# UPDAES THE FIRST VALUE BECAUSE IT HAS DUPLCIATE SO IT TAKES LAST DUPLICATE VALUES AS FIRST PREFERENCE AND OREDER THE ENTIRE DICT
#{1: 150, 2: 100, 4: 550}

SYNTAX TO GET ANY VALUE TO GET A VALUE FROM DICTIONARY

dictionaryname[key]

d = {1:100,2:100,4:550,10:150}
print(d[4]) # 550

# - we can get values by key 
# - but can't we get key by values

to update value:
    - dictionaryname[key] = newvalue
  
    Example: 
        d = {1:100,2:150,4:550,10:250}
        d[4] = 200
        print(d) # {1:100,2:150,4:200,10:250}


# take input from user side like how many input and each key value pair should enter by user

d = {}
num = int(input('enter Your input:'))
for i in range(num):
    key = eval(input(f"enter Your Keys {i+1}:"))
    value = eval(input(f'Enter your Values {i+1}:'))
    if type(key) not in [list,set,dict,float,complex]:
        d[key] = value
    else:
        print("Invalid datatype")
print(d)


enter Your input:3    
enter Your Keys 1:'Name'
Enter your Values 1:'Aakash'
enter Your Keys 2:'age'
Enter your Values 2:21
enter Your Keys 3:'skills'
Enter your Values 3:'Python'
{'Name': 'Aakash', 'age': 21, 'skills': 'Python'}

d = {'name':['Batman','Captain America'],'Marks':[99,99]}

for i in d:
    print(i,d[i])
    
d = {'name':['Batman','Captain America'],'Marks':[99,99]}
for i,j in [('name',['Batman','Captain America']),('Marks',[99,99])]:
    print(i)
    print(i,j)
    
for key,value in d.items():
    print(key,value)
print(d.items())


# list won't support in keys as we mentioned key's are immutable
# print(10==[10,10,30]) # both types of different so it returns False

## BUILD IN METHODS
    1) items
        - example
        d = {'name':['Batman','Captain America'],'Marks':[99,99]}
        for key,value in d.items():
            print(key,value)

    2) keys
        - example:
            d = {'name':['Batman','Captain America'],'Marks':[99,99]}
            print(d.keys())

    3) copy
        - example:
            d = {'name':['Batman','Captain America'],'Marks':[99,99]}
            res = d.copy()
            print(res)

    4) clear
        - example:
            d = {'name':['Batman','Captain America'],'Marks':[99,99]}
            res = d.clear()
            print(res) # None
            print(d) # {}
            
    5) pop
        - example:
            d = {'name':['Batman','Captain America'],'Marks':[99,99]}
            res = d.pop('name')
            print(res) # ['Batman', 'Captain America']
            print(d) # {'Marks': [99, 99]}
            
            res = d.pop('name_new' 'key is not present') --> it won't raise any error instead it prints the statement
            print(res)
            
    6) popitem
        - example:
            d = {'name':['Batman','Captain America'],'Marks':[99,99]}
            print(d.popitem()) # ('Marks', [99, 99]) --> removed value in form of tuple removes last value by default
            print(d) # {'name': ['Batman', 'Captain America']} --> remaining value in the dict
            
    7) update
        if key is there it update the values if there is no key it creates new kwy 
        - example:
            d = {'name':['Batman','Captain America'],'Marks':[99,99]}
            d.update({'city':{'Gotham','New York'}})
            print(d)
    
    8) setdefault
        it creates a default key value in end of the dict
        we can give only one pair for this setdefault
        - example:
            d = {'name':['Batman','Captain America'],'Marks':[99,99]}
            d.setdefault('name1':100)
            print(d) # {'name':['Batman','Captain America'],'Marks':[99,99],'s_name':100}
            
    9) get
        get the particular value based on the keys
        if we entred any other value which is not present in dict it won't raise any error it returns None because default it will be None
        but we can custmize anything istead of None
        - example:
            d = {'name':['Batman','Captain America'],'Marks':[99,99]}
            res = d.get('name','key is not present')
            print(res) # ['Batman', 'Captain America']
            
    10) fromkeys
        it creates a dictionary with a default value for all the keys and inside from keys it only accepts collection
        l = ['batman','spiderman','hulk']
        d = {}.fromkeys(l,['present']) --> instead of default we use our own statement
        print(d)
        
## SIMILAR WAY FOR LIST AND TUPLE

l = ['batman','spiderman','hulk']
d = {}.fromkeys(l,['present']) 
# --> instead of default we use our own statement
print(d)

l = ['batman','spiderman','hulk']
d={}
for i in l:
    d[i]='default'
print(d)


l = ('batman','spiderman','hulk')
d={}
for i in l:
    d[i]='default'
print(d) 

# dict comprension
# d = {k:k+10 for k in range(10)}
# print(d) # {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}


# take list of random names string value 
# input --> l = ['batman','spiderman','hulk']
# expected output --> d = {'batman':4,'spiderman':8,'hulk':3}


# normal code

l = ['batman', 'spiderman', 'hulk']
d = {}
for name in l:
    d[name] = len(name)
print(d)

l = ['batman', 'spiderman', 'hulk']
d = {k:len(k) for k in l}
print(d)       

"""

# def add(a,b):
#     return a+b
# print(add(1,2))
# print(add(10,23))

# assignmet update the values without using build in methods and for set default also
# assignmet upper character without build in method for isupper also
