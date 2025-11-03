"""Types of arguments:
    - positional arguments
    - default arguments
    - keyword arguments
    - variable length arguments ( *args, **kwargs )"""
    
# 1) positional arguments :

def add(a,b):  # positional arguments
    return a+b
print(add(2,3))  # 2,3 are positional arguments

# 2) default arguments :

def add(a=2,b=3):  # default arguments
    return a+b
print(add())  # if we don't pass any arguments it will take default values
print(add(5))  # if we pass one argument it will take that value for a and default value for b
print(add(5,6))  # if we pass two arguments it will take those values


# poistional arguments can't follow default arguments
# def add(a=2,b):  # default arguments
#     return a+b
# print(add(5))  # it will give error because positional arguments can't follow default arguments

# def add(b,a=2):  # default arguments
#     return a+b
# print(add(5))  # it will work because default arguments are at the end

# 3) keyword arguments :

def add(a,b):  # keyword arguments
    return a+b
print(add(b=3,a=2))  # we can pass arguments in any order using keyword arguments
print(add(a=2,b=3))  # we can pass arguments in any order using keyword arguments
print(add(2,b=3))  # we can mix positional and keyword arguments but positional
# arguments should be at the beginning
# print(add(a=2,3))  # it will give error because positional arguments should be at the beginning

# def fun(a,b):
#     print(a,b)
# fun(b=2,3)  # it will give error because positional arguments should be at the beginning
# fun(3,b=2)  # it will work because positional arguments are at the beginning

# 4) variable length arguments :

        # - it stores only "positional arguments" in the form of tuple by using of *args
        # - it stores only "keyword arguments" in the form of dictionary by using of **kwargs
    
# arbitrary arguments (or) *args (non keyword arguments)

def add(*args,s):
    print(type(args),args)  # args will be treated as tuple
add(1,2,3,4,5,s=10)  # we can pass any number of arguments but s is a keyword argument so we need to pass it as keyword argument

def add(*args):  # *args (non keyword arguments)
    total = 0
    for i in args:
        total+=i
    return total
print(add(1,2,3,4,5))  # we can pass any number of arguments # (1,2,3,4,5) will be treated as tuple
print(add(10,20))  # we can pass any number of arguments
print(add())  # we can pass any number of arguments including zero arguments    

# **kwargs (keyword arguments)

def person(**kwargs):  # **kwargs (keyword arguments)
    for key,value in kwargs.items():
        print(f'{key} : {value}')
person(name='John',age=30,city='New York')  # we can pass any number of keyword arguments
person(name='Alice',age=25)  # we can pass any number of keyword arguments

def add(**kwargs):
    print(type(kwargs),kwargs)  # kwargs will be treated as dict
add(a=1,b=2,c=3) 

def add(*args, **kwargs):
    print(type(args), args) # <class 'tuple'> (1, 2, 3)  # args will be treated as tuple
    print(type(kwargs), kwargs) # <class 'dict'> {'a': 4, 'b': 5}  # kwargs will be treated as dict
    print(args, kwargs) # (1, 2, 3) {'a': 4, 'b': 5}
add(1,2,3,a=4,b=5)

# get the average of values using *args and **kwargs without build in methods

def average(*args, **kwargs):
    total = 0
    count = 0
    for i in args:
        total+=i
        count+=1
    for value in kwargs.values():
        total+=value
        count+=1
    return total/count if count != 0 else 0  # to avoid division by zero error
print(average(1,2,3,a=4,b=5))  # (1+2+3+4+5)/5 = 3.0

# explaination of above code
# def average(*args, **kwargs):
#     total = 0
#     count = 0
#     for i in args:  # args = (1,2,3)
#         total+=i  # total = 1+2+3 = 6
#         count+=1  # count = 3 # count of args
#     for value in kwargs.values():  # kwargs = {'a':4,'b':5}
#         total+=value  # total = 6+4+5 = 15
#         count+=1  # count = 3+2 = 5 # count of kwargs values
#     return total/count if count != 0 else 0  # return 15/5 = 3.0
# print(average(1,2,3,a=4,b=5))  # (1+2+3+4+5)/5 = 3.0

# why we are using if count != 0 else 0 in return statement because if we don't pass any arguments it will give error because of division by zero so to avoid that we are using if count != 0 else 0


def fun(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
print(fun(1,2,3,4,5))  # 15

def fun2(**kwargs):
    sum = 0
    for value in kwargs.values():
        sum+=value
    return sum
print(fun2(a=1,b=2,c=3))  # 6

# (or)

def fun2(**kwargs):
    sum = 0
    for key in kwargs:
        sum+=kwargs[key]
    return sum
print(fun2(a=1,b=2,c=3))  # 6

# explaination of above code
# def fun2(**kwargs):  # kwargs = {'a':1,'b':2,'c':3}
#     sum = 0
#     for key in kwargs:  # key = 'a','b','c'
#         sum+=kwargs[key]  # sum = 1+2+3 = 6
#     return sum
# print(fun2(a=1,b=2,c=3))  # 6
# how it extract values from dictionary using keys kwargs[key]
# it uses the key to access the value in the dictionary
# kwargs = {'a':1,'b':2,'c':3}
# key = 'a'
# kwargs[key] = kwargs['a'] = 1
# key = 'b'
# kwargs[key] = kwargs['b'] = 2
# key = 'c'
# kwargs[key] = kwargs['c'] = 3
# so it will add all the values in the dictionary and return the sum
