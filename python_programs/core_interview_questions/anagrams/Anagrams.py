## Sorting is O(n log n) in time complexity.

s1 = input("enter a string 1:")
s2 = input("enter a string 2:")

if sorted(s1) == sorted(s2):
    print("both string are Anagrams")

else:
    print("both string are not Anagrams")
    

# 2. Using collections.Counter

# More efficient for large strings (O(n)).
# Works well with repeated characters.

from collections import Counter

if Counter(s1) == Counter(s2):
    print("Anagrams")
else:
    print("Not Anagrams")


# Using set and count

if set(s1) == set(s2) and all(s1.count(c) == s2.count(c) for c in set(s1)):
    print("Anagrams")
else:
    print("Not Anagrams")
