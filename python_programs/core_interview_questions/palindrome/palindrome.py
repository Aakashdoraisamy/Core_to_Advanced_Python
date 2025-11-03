def ispalindrome(s):
   return s == s[::-1]
s = input("enter a name:")
ans = ispalindrome(s)
if ans:
    print("it's is a palindrome ")
else:
    print("it's is not palindrome")

# 2nd way

name = input("enter the data:")
if(name == name[::-1]):
    print("it is palindrome")
else:
    print("it is not paindrome")
    
# using reverse method

s = input("Enter a string: ")

if s == ''.join(reversed(s)):
    print("Palindrome")
else:
    print("Not Palindrome")


# For Numbers (without converting to string, using math)

n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
