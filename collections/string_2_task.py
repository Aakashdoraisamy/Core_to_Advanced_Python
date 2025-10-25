# # write a program to sum the two numbers without using + operator

a = int(input('Enter first number:')) # 7
b = int(input('enter Second number:')) # 5
l1 = '0' * a # '0000000'
l2 = '1' * b # '11111'
print(len(f'{l1}{l2}')) # '000000011111' # 12

# # print odd or even number without using if

a = ['even','odd']
print(f'the entered number is {a[int(input("Enter a number:"))%2]}')

## split without using split built in function

s = input('Enter a string with spaces:')
l = []
word = ''
for char in s:
    if char != ' ':
        word += char
    else:
        l.append(word)
        word = ''
l.append(word)
print(l)

## pattern

n = int(input('Enter a number:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
## factorial

def factorial(num):
    result = 1
    while num>=1:
        result = result*num
        num -= 1
    return result
print(factorial(int(input('Enter a number:'))))

## factors

def print_factors():
    n = int(input('Enter a number:'))
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    return l
print(print_factors())

## fibonacci series

def fibonacci(n):
    a,b = 0,1
    l = []
    for i in range(n):
        l.append(a)
        a,b = b,a+b
    return l
print(fibonacci(int(input('Enter a number:'))))

