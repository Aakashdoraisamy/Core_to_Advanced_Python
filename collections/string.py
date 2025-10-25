"""
## STRINGS
    -- Properties
        - String is Homogeneous Collection
        - It is an ordered collection
        - it supports duplicates
        - indexing and slicing are supports
        - string is an immutable
        - updation and deletion is not possible
        
        how to extract a value by using loop
        
        s = 'Pyspiders'
        for i in s:
            print(i, end = ' ')
         
         
# PROGRAMS

# s = input("Enter your Input: ")
# for i in s:
#     if ('A' <= i <= 'Z') or ('a' <= i <= 'z'):
#         if i in 'AEIOUaeiou':
#             print("It is Vowel")
#         else:
#             print("It is Consonant")
#     else:
#         print("It is not an alphabet")

# REVERESE A STRING

# s = input('Enter a String:').lower()
# output = ''
# i = len(s)-1
# while i>=0:
#     output += s[i]
#     i = i-1
# print(output)    

# s = "hello"
# rev = ""
# for i in s:
#     rev = i + rev  
# print(rev) 

# ------------------------------------------------ ################################### -------------------------------- #

BUILD IN METHODS

    1) upper
    
        Returns Everything as uppercase            
        s = 'batman'
        print(s.upper()) # BATMAN
        
    2) isupper
    
        checks is the given string is upper or not
        s = 'batman01'
        print(s.isupper()) # False --> only consider alphabets only ignores digits and special case
        
    3) lower
    
       Returns Everything as lowercase
       s = 'BATMAN'
       print(s.lower()) # batman
       
    4) islower
        
       checks is the given string is lower or not        
       s = 'batman01'
       print(s.islower()) # True
       
    5) title

       changes each word first letter or character as upper case
       s = 'batman superman'
       print(s.title()) # Batman Superman
       
    6) istitle
    
       checks each word first char is upper or not
       s = 'batman superman'
       print(s.istitle()) # False
       
    7) capitalize
    
        returns capitalize for entire string for first char only
        s = 'batman superman'
        print(s.capitalize()) # Batman superman
        
    8) isdecimal
    
        checks is it decimal or not inside in the string if all the char is num it returns True
        example:
            s0 = '123'
            s1 = '123.32'
            s2 = '123.A2'
            s3 = '2/3' --> everything consider as char including / so it returns false
            print(s0.isdigit()) # True
            print(s1.isdigit()) # False
            print(s2.isdigit()) # False
            print(s3.isdigit()) # False
            
    9) isalpha

        check is the given string is alphabet or not
        example:
        s1 = 'Aakash'
        s2 = 'abc@123'
        print(s1.isalpha()) # True
        print(s2.isalpha()) # False
        
    10) isalnum
    
        checks is the given string either alphabet or num
        example:
            s1 = 'Aakash123'
            s2 = 'Aakash@123'
            s3 = '123'
            s4 = 'Aakash'
            print(s1.isalnum()) # True
            print(s2.isalnum()) # False
            print(s3.isalnum()) # True
            print(s4.isalnum()) # True
            
    11) count

        check how many times the character is present
        it returns the occurence(frequency|count) of a character
        stringname.count() --> returns int
        
        example:
            print('Aakash'.count('a')) # 2 consider 2 only
            
    12) index
    
        to find the particular character
        
        example:
            print('Aakash'.index('a')) # 1 consider first occurence
            
    13) split
    
        to split the characters
        no need to pass empty string but we can give empty string with space we should pass atleast one value
        
        example:
        print('Aakash ECE'.split(',')) #['Aakash ECE']
        print('Aakash ECE'.split()) #['Aakash','ECE']
        
        s = 'py spiders btm'.split(s) # ['py ','pider',' btm']
        print('$'.join(s)) # 'py $pider$ btm'
        
    14) join

        only string values only applicable
        it returns string
        syntax:
            ''.join(values)
            
        example:
            s = 'py spider btm'.split()
            print('-'.join(s)) # 'py-spider-btm'
            print(' '.join(s)) # 'py spider btm'
            


        
"""

# Assignment 
# take a string from user split the words convert words to upper case if that word is present in even index once operation was done combine all values by join

"""
    user input:
    
    1) 'py spiders btm'
    
    o/p -> [2,7,3]
    
    2) py-2 spiders-7 btm-3
    
    3) py sredips btm
    
    4) [py,ss,bm]
    
"""

# s = 'py spiders btm'
# l = []
# words = s.split(' ')
# for w in words:
#     l.append(len(w))
# print(l)
# #       (or)
# print([len(w) for w in words])

# s = 'py spiders btm'
# l = []
# words = s.split(' ')
# for w in words:
#     l.append(f"{w}-{len(w)}") 
# print(' '.join(l)) 


# s = 'py spiders btm'.split()
# l = [len(i) for i in s]
# print(l)

# s = 'py spiders btm'.split()
# l = [f'{i}-{len(i)}' for i in s]
# print(l)
