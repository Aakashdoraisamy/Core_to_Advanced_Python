#prime number

number = int(input("enter any positive number:"))
for i in range(2,number):
    if number % i == 0:
        print("it is not prime number")
        break
else:
        print("it is prime number")
        
        
# 2nd way 
        
n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")



# Optimized trial division (up to √n)

n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# Using a Function

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print("Prime" if is_prime(n) else "Not Prime")


# Using all() with list comprehension

n = int(input("Enter a number: "))

if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
    print("Prime")
else:
    print("Not Prime")


# Using recursion (less common)

def check_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return check_prime(n, i + 1)

n = int(input("Enter a number: "))
print("Prime" if check_prime(n) else "Not Prime")
