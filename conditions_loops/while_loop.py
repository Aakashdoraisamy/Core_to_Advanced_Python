# WHILE LOOP

# to extract directly characters from a string in while loop not posslible like in for loop but we can we use indexing

# we use wile loop in two scenarios
# 1. when we dont know the number of iterations
# 2. when we want to use break and continue statements

"""
step 1
start value -> start_value = 0

step 2
while condition -> while start_value < len(s):
    #statements
    
step 3
    updation -> start_value += 1
    
"""

# s = int(input('Enter a number:'))
# while s<=10:
#     print(s)
#     s+=1
    
# this 4 lines internally works in for loop

# take input from user start value and end value and just check the values which are divisible by 3 and 8 using while loop

start = int(input('Enter Start Value:'))
end = int(input('Enter End Value:'))
count = 0
while start<=end:
    if start%3 == 0 and start%8 == 0:
        print(start)
        count+=1
    start+=1
print(f'Count of numbers divisible by 3 and 8 from {start} to {end} is : {count}')


# BANK QUESTION

bal = int(input('Enter your Balance:'))
while True:
    option = int(input('1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit\nEnter your option:'))
    match option:
        case 1:
            amt = int(input('Enter Amount:'))
            if 0<=amt<=bal:
                bal-=amt
                print(f'Your Balance after withdraw is {bal}')
                break
            else:
                print('Insufficient Balance')
        case 2:
            amt = int(input('Enter Amount:'))
            if 0<=amt<=5000:
                bal+=amt
                print(f'Your Balance after Deposit is {bal}')
                break
            else:
                print('Deposit limit exceeded')
        case 3:
            print(f'Your Balance is {bal}')
            break
        case _:
            print('Invalid Option')

# start = 10
# while start <= 18:
#     if start == 15:
#        break
#     print(start)
#     start += 1

# start = 10
# while start <= 18:
#     if start == 15:
#        start += 1
#        continue
#     print(start)
#     start += 1
    
# start = 10
# while start <= 18:
#     if start == 15:
#        pass
#     print(start)
#     start += 1


#take 1 number from user and add odd numbers till that number

s = int(input('Enter a number:'))
sum = 0 # to store the sum of odd digits
while s>0: # loop will run until s becomes 0
    r = s%10 # extracts the last digit
    if s%2 != 0: # checks whether the digit is odd or not
        sum+=r # adds the odd digit to sum
    s = s//10 # removes the last digit
print(f'Sum of odd digits is {sum}') # prints the sum of odd digits

# NESTED LOOP
# n = int(input('Enter a number:'))
# for i in range(3):
#     for j in range(4):
#         print(n, end= ' ')
#         n+=1
#     print()

