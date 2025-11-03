r"""
types of scope:
    - local scope
    - global scope
    - nonlocal scope

    
# Global scope:
    
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