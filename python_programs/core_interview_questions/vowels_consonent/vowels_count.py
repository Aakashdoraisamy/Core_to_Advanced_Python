vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)

# > 3

s = input('Enter a String:')
count = 0
for char in s:
    if char in 'aeiouAEIOU':
        count+=1
print(f'Count of Vowels in {s} is {count}')