def factorial(num):
    result = 1
    while num>=1:
        result = result*num
        num -= 1
    return result
print(factorial(int(input('Enter a number:'))))