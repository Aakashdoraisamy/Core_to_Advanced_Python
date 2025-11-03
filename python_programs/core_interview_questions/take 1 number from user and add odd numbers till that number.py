#take 1 number from user and add odd numbers till that number
s = int(input('Enter a number:'))
sum = 0 # to store the sum of odd digits
while s>0: # loop will run until s becomes 0
    r = s%10 # extracts the last digit
    if s%2 != 0: # checks whether the digit is odd or not
        sum+=r # adds the odd digit to sum
    s = s//10 # removes the last digit
print(f'Sum of odd digits is {sum}') # prints the sum of odd digits