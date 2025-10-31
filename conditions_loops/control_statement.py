# CHECKS IF TWO VARIABLES POINT TO THE SAME OBJECT IN MEMORY

a = int(input('Enter First Number:'))
b = int(input('Enter Second Number:'))
if id(a) == id(b):
    print('Both of Adrress are same')
else:
    print('Both are Not same')

# CHECKS IF THE LAST DIGIT OF A NUMBER IS 5 OR NOT

num = int(input("Enter an integer: "))
digit = num % 10
if digit == 5:
    print("Batman")
else:
    print("The last digit is:", digit)

# CHECKS IF A CHARACTER IS UPPERCASE OR LOWERCASE

char = input("Enter a character: ")
if char == char.upper():
    print("Uppercase")
else:
    print("Lowercase")
    
# if 65 <= ascii_value <= 90:

# 1st way

char = input("Enter a character: ")
ascii_value = ord(char)
if ascii_value >= 65 and ascii_value <= 90:
    print(f"{char} is uppercase")
else:
    print(f"{char} is not uppercase")
    
# print(ord('A'), ord(c),ord('Z'))

# 2nd way

char = input("Enter a character: ")
if char>= 'A' and char <= 'Z':
    print(f"{char} is uppercase")
elif char >= 'a' and char <= 'z':
    print(f"{char} is not uppercase")
else:
    print("Invalid input")

# 3rd way

char = input("Enter a character: ")

if 'A' <= char <= 'Z':
    print(f"{char} is uppercase")
else:
    print(f"{char} is not uppercase")

# CHECKS IF A CHARACTER IS A VOWEL OR A CONSONANT

# 1st way

c = input("Enter a character: ")
if c in 'AEIOUaeiou':
    print(f"{c} is a vowel")
else:
    print(f"{c} is a consonant")
    
# 2nd way

c = input("Enter a character: ").lower()
if c in 'AEIOU':
    print(f"{c} is a vowel")
else:
    print(f"{c} is a consonant")


# CHECKS IF A NUMBER IS A DIVISIBLE OR NOT

number = int(input("enter any positive number:"))
for i in range(2,number):
    if number % i == 0:
        print("it is not prime number")
        break
else:
        print("it is prime number")
        
prime = int(input("Enter a number: "))
if prime%3 == 0 or prime%7 == 0:
    print(f"{prime} is a Divisible by 3 and 7")
else:
    print(f"{prime} is not Divisible by 3 and 7")
    
    
# CONVERTS A UPPERCASE CHARACTER TO LOWERCASE

# 1st way

c = input("Enter a character: ")
if c>= 'A' and c <= 'Z':
    ord_val = ord(c)+32 
# --> 65+32=97
    c_val = chr(ord_val) 
# --> chr(97) = 'a'
    print(c_val)
else:
    print("not valid")
    
# 2nd way

c = input("Enter a character: ")
if c>= 'A' and c <= 'Z':
    print(chr(ord(c)+32))
else:
    print("not valid")


# CHECKS THE CHARACTER IS AN ALPHABET OR NOT AND CONVERTS LOWERCASE TO UPPERCASE AND UPPERCASE TO LOWERCASE

# 1st way

c = input("Enter a character: ")
if c>= 'A' and c <= 'Z':
    ord_val = ord(c)+32 
    c_val = chr(ord_val) 
    print(c_val)
elif c>= 'a' and c <= 'z':
    ord_val = ord(c)-32 
    c_val = chr(ord_val) 
    print(c_val)
else:
    print("Given input is not an alphabet")

# 2nd way

c = input("Enter a character: ")
if c>= 'A' and c <= 'Z':
    print(chr(ord(c)+32))
elif c>= 'a' and c <= 'z':
    print(chr(ord(c)-32))
else:
    print("Given input is not an alphabet")

# CHECKS THE INPUT IS SINGLE OR DUBLE DIGIT OR THRIPPLE DIGIT NUMBER AND CHECKS NEGATIVE AND POSTIVE    

num = int(input("Enter a number: "))
if (num >= 0 and num <= 9) or (num >= -9 and num <= 0): 
    print(f"{num} is a single digit number")
elif (num >= 10 and num <= 99) or (num >= -99 and num <= -10): 
    print(f"{num} is a double digit number")
elif num >= 100 and num <= 999 or (num >= -999 and num <= -100):
    print(f"{num} is a triple digit number")
else:
    print("Invalid input")    

# NESTED IF ELSE

num = int(input('Enter a Number:'))
if num%7 == 0:
    if num%4 == 0:
        print(f'{num} is divisible by 7 and 4')
    else:
        print(f'{num} is divisible by 7 but not by 4')
else:
    if num%4 == 0:
        print(f'{num} is not divisible by 7 but divisible by 4')
    else:
        print(f'{num} is not divisible by 7 and 4')

# TAKE A CHARACTER FROM USER AND CHECKS IT IS ALPHAET OR NOT AND IF IT IS ALPHABET THEN CHECKS IT IS VOWELS OR CONSONANT AND THEN CHECKS IT IS NUMBER OR SPECIAL CHARACTER  

c = input("Enter a character: ")
if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
    if c in 'AEIOUaeiou':
        print(f"{c} is a vowel")
    else:
        print(f"{c} is a consonant")
elif c >= '0' and c <= '9':
    print(f"{c} is a number")
else:
    print("Special character")
    
    
"""
MATCH CASE STATEMENT
syntax:
option = int(input())
match option:
    case 1:
        # do something
    case 2:
        # do something
    case _:
        # default case
    .
    .
    .
    .
    case _:
        # default case    
"""

option  = int(input("Enter any option: "))
match option:
    case 1:
        print('Leonardo DiCaprio')
    case 2:
        print('Brad Pitt')
    case 3:
        print('Kane Williamson')
    case 4:
        print('Martin Scorsese')
    case _:
        print('Invalid option')
