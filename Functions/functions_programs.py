# Factorial Using Loop

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))


# Factorial Using Recursion

def factorial(n):
    if n == 0 or n == 1:     # base case
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))


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

# Print All Factors of a Number

def print_factors(n):
    print("Factors of", n, "are:", end=" ")
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")

num = int(input("Enter a number: "))
print_factors(num)


# Sum of Natural Numbers Using Recursion

def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

print(sum_natural(int(input("Enter n: "))))

# Fibonacci Series Using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter number of terms: "))
for i in range(num):
    print(fibonacci(i), end=" ")

# Recursive Function to Find GCD (Greatest Common Divisor)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD:", gcd(x, y))

