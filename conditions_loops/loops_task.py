# ASSIGNMENT

# one number should we take and reverse the number only using while loop

n = int(input('enter a Number:'))
while n>0:
    rem = n%10
    print(rem, end=' ')
    n = n//10

# num = int(input('Enter a number:'))
# rev = 0
# while num>0:
#     r = num%10
#     rev = rev*10 + r
#     num = num//10
# print(f'Reversed number is {rev}')

# WRITE A PROGRAM TO PRINT A PATTERN OF NUMBERS

n = int(input('Enter a number:'))
for i in range(3):
    for j in range(4):
        print(n, end= ' ')
        n+=1
    print()


# write a program to print a pattern of characters

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        if i%2 == 0:
            print('?', end= ' ')
        else:
            print('#', end= ' ')
    print()
    
    
# write a program to print a pattern of characters

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        if j % 2 == 0:  
            print("@", end=" ")
        else:          
            print("*", end=" ")
    print()


# take input from user side check it is odd or even and then count sum and average of odd and even numbers separately

num = int(input('Enter a number:'))
even_count , odd_count , even_sum , odd_sum = 0,0,0,0
while num > 0:  
# (0r) != 0:
    r = num % 10
    if r % 2 == 0:
        even_count += 1
        even_sum += r
    else:
        odd_count += 1
        odd_sum += r
    num = num // 10
print(f'Count of even numbers is {even_count} and Sum of even numbers is {even_sum} and Average of even numbers is {even_sum/even_count if even_count > 0 else 0}')
print(f'Count of odd numbers is {odd_count} and Sum of odd numbers is {odd_sum} and Average of odd numbers is {odd_sum/odd_count if odd_count > 0 else 0}')
    
# Perfect Numbers 1 to 10000

# Program to find perfect numbers from 1 to 10000

num = 1 

while num <= 10000:
    sum_of_divisors = 0
    i = 1
    while i < num: 
        if num % i == 0:
            sum_of_divisors += i
        i += 1
    if sum_of_divisors == num:
        print(f"{num} is a perfect number")
    num += 1
