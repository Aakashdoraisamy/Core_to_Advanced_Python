word = input("enter any set:")

s = set(word)

vowels = {'a','e','i','o','u','A','E','I','O','U'}

result = s.intersection(vowels)

print(result)
print('The differnt vowels {} present in {}'.format(word,result))