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
        - recursive functions
        
        examples:
        
        1) with arguments and with return type
        
        def add(a,b): 
            return a,b,a+b # if we give multiple values it will return as tuple
        print(add(2,3))
        
        2) with arguments and without return type
        
        def add(a,b):  
            print(a+b)
        add(2,3)

        3) without arguments and with return type
        
        def get_name():
            name = "Aakash"
            return name

        result = get_name()
        print("Name is:", result)

        4) without arguments and without return type
        
        def greet(): 
            print('Hello, Good Morning!')
        greet()
            
# n = int(input('Enter a number:'))
# if user enter 10 
# print(1,2,3,10)

1) with arguments and without return type

def print_numbers(n):
    for i in range(1,n+1):
        if n%i == 0: 
            print(i, end=" ")
print_numbers(int(input('Enter a number:')))

# n%i == 0 will print all the factors of n example n = 10 and i = 1,2,5,10 how it is working because 10%1 == 0, 10%2 == 0, 10%5 == 0, 10%10 == 0

2) without arguments and with return type

def print_factors():
    n = int(input('Enter a number:'))
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    return l
print(print_factors())

3) with arguments and with return type

def print_factors(n):
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    return l
print(print_factors(int(input('Enter a number:'))))

4) Without arguments and without return type

def print_factors():
    n = int(input('Enter a number:'))
    print("Factors of", n, "are:", end=" ")
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")
print_factors()

"""


