"""
## Functions

    - it is a block of code used for code reusability
    
    types of functions:
        - user defined functions
        - built in functions (predefined functions)
        - anonymous functions (lamda functions)
        
user defined functions:

    - created by the user to perform a specific task
    - def keyword is used to define a function
    - function name should be meaningful and should follow the variable naming conventions
    - function can have parameters (optional)
    - the default return type of a function is "None" if there is no return statement in the function
    
      syntax:
        def function_name(parameters):
            '''docstring (optional)'''
            statement(s)
        print(function_name(arguments))
        
       example:
       
        def add(a,b):   --> a,b are parameters
            return a+b
        print(add(2,3))  --> 2,3 are arguments

        def add(a,b):
            print(a+b)  --> if we use print instead of return it will return None
        add(2,3)
        
        def add(a,b):
            return a+b
        add(2,3)  --> it will return None because we are not printing the return value
        add(int(input('Enter a:')), int(input('Enter b:'))) --> it will return None because we are not printing the return value
        
        def add(a,b):
            print(a+b)
        res = add(2,3)
        print(res) # 5 
                   # None
                   
# Types of User defined functions:
        - with arguments and with return type
        - with arguments and without return type
        - without arguments and with return type
        - without arguments and without return type
        - recurssive functions
        
        example:
        def add(a,b):  # with arguments and with return type
            return a,b,a+b # if we give multiple values it will return as tuple
        print(add(2,3))
        
        def add(a,b):  # with arguments and without return type
            print(a+b)
        add(2,3)
        
        def greet():  # without arguments and with return type
            return 'Hello, Good Morning!'
        print(greet())
        
        def greet():  # without arguments and without return type
            print('Hello, Good Morning!')
        greet()
            
# n = int(input('Enter a number:'))
# if user enter 10 
# print(1,2,3,10)

# with arguments and without return type

def print_numbers(n):
    for i in range(1,n+1):
        # if i == n or i <= 3:
        if n%i == 0: # n%i == 0 will print all the factors of n example n = 10 and i = 1,2,5,10 how it is working because 10%1 == 0, 10%2 == 0, 10%5 == 0, 10%10 == 0
            print(i, end=" ")
print_numbers(int(input('Enter a number:')))


# without arguments and with return type
def print_factors():
    n = int(input('Enter a number:'))
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    return l
print(print_factors())

#with arguments and with return type
def print_factors(n):
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    return l
print(print_factors(int(input('Enter a number:'))))

Types of arguments:
    - positional arguments
    - default arguments
    - keyword arguments
    - variable length arguments ( *args, **kwargs )
    
## positional arguments :

def add(a,b):  # positional arguments
    return a+b
print(add(2,3))  # 2,3 are positional arguments

## default arguments :

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

## keyword arguments :

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

## variable length arguments :

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

### types of scope:
    - local scope
    - global scope
    - nonlocal scope
    
    ## Global scope:
    
    - we can access the variable anywhere in the program and we can access methods and functions also
    - variable declared outside the function is called global variable
    - global variable can be accessed inside the function
    - if we want to modify the global variable inside the function we need to use global keyword
    - if we don't use global keyword it will create a new local variable with the same name as global variable  
    
    s = 8080
    def fun():  --> func is global function or scope
        global s  
        print(s)  # 8080
        
    def fun2():
        print(s)
    fun2() # 8080
    
    fun2()
    def fun3():
        fun2()
        print(s,'fun3()')
    fun3() # 8080
           # 8080 fun3()

## Local scope:
    
    - we can access the variable only inside the function
    - variable declared inside the function is called local variable
    - local variable can't be accessed outside the function
    - if we try to access the local variable outside the function it will give error
    
    def fun4():
        s = 9090  # local variable
        print(s)  # 9090
    fun4()  # 9090
    print(s)  # error because s is not defined in global scope
    
    s = 500
    def fun():
        s = 600  # local variable
        print(s)  # 600
    print(s)  # 500
    fun()  # 600
    print(s)  # 500

    # output:
    # 500
    # 600
    # 500

## global keyword:

    def fun():
        global s  
        s = 9090  # it will modify the global variable
        print(s)  # 9090
    fun()  # 9090
    print(s)  # 9090
    
    s = 500
    def fun():
        global s  
        s = 600  # it will modify the global variable
        print(s)  # 600 
    fun()
    print(s)
    
    # output:
    # 600
    # 600

## globals 
        
    - this method returns all built in variables and methods in the form of dictionary
    - it returns user defined functions and it's address, variable name and it's value
    - it can access only outside the function    
        
    x = 10
    def fun1():
        print(x)  # 10
    fun1()
    print(x)
    print(globals())  # it will print all the global variables and functions in the form of dictionary
    print(type(globals()))  # <class 'dict'>

## locals

    - this method should access only inside the function
    - if we access outside the function it will acts as globals method
    
    def fun2():
        a = 20
        b = 30
        print(locals())  # it will print all the local variables in the form of dictionary
        print(type(locals()))  # <class 'dict'>
    fun2()


x = 10
def fun1():
    print(x)  # 10
res = fun1
print(res)  # <function fun1 at 0x00000221DBCCCA40>

def fun():
    global s  
    s = 600  # it will modify the global variable
    print(s)  # 600
fun()
print(s)  # 600
res = fun
res1 = res
res()
res1()

## nonlocal scope:

    - it is used to access the variable from the nearest enclosing scope
    - it is used in nested functions
    - if we want to modify the variable from the nearest enclosing scope we need to use nonlocal keyword
    - if we don't use nonlocal keyword it will create a new local variable with the same name as enclosing scope variable
    
    def outer():
        s = 8080  # enclosing scope variable
        def inner():
            nonlocal s  
            s = 9090  # it will modify the enclosing scope variable
            print(s)  # 9090
        inner()
        print(s)  # 9090
    outer()
    
    # output:
    # 9090
    # 9090
    
    def outer():
        s = 8080  # enclosing scope variable
        def inner():
            s = 9090  # local variable
            print(s)  # 9090
        inner()
        print(s)  # 8080
    outer()
    
    # output:
    # 9090
    # 8080

"""

# write a program fro perfect numbers 1 to 10000 using def and for loop

# n = 6
# 1 +2 + 3 = 6
# 1) create a fucntion it should return true or false based on perfect number logic
# 2) by using for loop generate the numbers from 1 to 10000 
#  check by using if keyword next to if just call the function and function will return true or false
#  if true store in a list

# def is_perfect(num):
#     total = 0
#     for i in range(1,num):
#         if num%i == 0:
#             total+=i
#     return total == num
# perfect_numbers = []
# for j in range(1,10001):
#     if is_perfect(j):
#         perfect_numbers.append(j)
# print(perfect_numbers)  # [6, 28, 496, 8128]
# is_perfect(6)  # True


# explaination of above code
# def is_perfect(num):  # num = 6
#     total = 0
#     for i in range(1,num):  # i = 1,2,3,4,5
#         if num%i == 0:  # 6%1==0, 6%2==0, 6%3==0
#             total+=i  # total = 1+2+3 = 6
#     return total == num  # return 6==6 = True
# perfect_numbers = []
# for j in range(1,10001):  # j = 1,2,3,...,10000
#     if is_perfect(j):  # check if j is perfect number
#         perfect_numbers.append(j)  # if true append to the list
# print(perfect_numbers)  # [6, 28, 496, 8128]  # perfect numbers between 1 to 10000


l = []
def perfect_number(n):
    sum = 0
    for i in range(1,n): # we don't want to include the last number because it is not a factor of itself
        if n%i == 0: # 6%1 == 0, 6%2 == 0, 6%3 == 0
            sum+=i
    return sum == n
for i in range(1,10001):
    if perfect_number(i):
        l.append(i)
print(l)
# print(perfect_number(int(input('Enter a number:'))))