# WRITE A PROGRAM TO ODD NUMBERS FROM 100 TO 10

for i in range(100, 9, -1):
    if i % 2 != 0:
        print(i, end=" ")

for i in range(99, 9, -2):
        print(i, end=" ")

s = input('Enter a String:')
i = 0
for x in s:
    print(f'Character at index {i} is {x}')
    i+=1


# WAP TO PRINNT THE COUNT OF NUMS DIV BY 3 AND 7 FROM START(USER INPUT) - END(USER INPUT)

start = int(input('Enter Start Range:'))
end = int(input('Enter End Range:'))
count = 0
for i in range(start, end+1):
    if i%3 == 0 and i%7 == 0:
        count+=1
print(f'Count of numbers divisible by 3 and 7 from {start} to {end} is : {count}')

# if we give print inside the loop it will print all the numbers which are divisible by 3 and 7 it will return 0 until count increases like
# start = 1
# end = 20
# count 0
# 0
# 0
# .
# .
# until 20
# then 21 will divisible by 3 and 7 so count will increase to 1
# and then 1
# 1
# 1
# .
# .
# until end so we need to give print outside the loop


# WRITE A PROGRAM TO FIND THE SUM AND AVERAGE OF N NUMBERS (N IS USER INPUT)

user = int(input('Enter a number:'))
total = 0
for i in range(1,user+1):
    total+=int(input(f'Enter number {i}:'))
print(f'Sum is {total} and Average is {total/user}')

s = input('Enter a String:')
count = 0
for char in s:
    if char in 'aeiouAEIOU':
        count+=1
print(f'Count of Vowels in {s} is {count}')

# WRITE A PROGRAM TO REVERSE A STRING USING FOR LOOP ITERABLE

# 1ST WAY

s = input('Enter a String:')
rev = ''
for char in s:
    rev = char + rev
print(rev)
    
# 2ND WAY

s = input('Enter a String:')
rev = s[-1:-len(s)-1:-1]
for char in rev:
    print(char)
   
# 3RD WAY    

s = input('Enter a String:')
rev = s[::-1]
for char in rev:
    print(char)

n = int(input("Enter how many numbers: "))

total = 0
for i in range(n):
    num = int(input("Enter number: "))
    total = total + num

print("Final answer:", total)

text = input("Enter something: ")

open_count = 0
close_count = 0

for ch in text:
    if ch == '{':
        open_count += 1
    elif ch == '}':
        close_count += 1

print("Number of { :", open_count)
print("Number of } :", close_count)
