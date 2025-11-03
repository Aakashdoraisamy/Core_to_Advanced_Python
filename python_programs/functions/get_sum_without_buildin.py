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
    return total/count 
print(average(1,2,3,a=4,b=5))  # (1+2+3+4+5)/5 = 3.0

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