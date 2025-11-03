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
    
# 3rd way

data = input("enter a data:")
vowels = ('a','e','i','o','u','A','E','I','O','U')
if data in vowels:
    print("it is a vowel")
else:
    print("it  is not a vowel")