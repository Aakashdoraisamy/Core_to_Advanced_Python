def fibonacci(n):
    a,b = 0,1
    l = []
    for i in range(n):
        l.append(a)
        a,b = b,a+b
    return l
print(fibonacci(int(input('Enter a number:'))))


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)
