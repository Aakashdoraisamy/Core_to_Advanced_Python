def fibonacci(n):
    a,b = 0,1
    l = []
    for i in range(n):
        l.append(a)
        a,b = b,a+b
    return l
print(fibonacci(int(input('Enter a number:'))))