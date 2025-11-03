word = input('Enter any String:')

vowels = {'a','e','i','o','u','A','E','I','O','U'}

d = {}

for ch in word:

    if ch in vowels:

        d[ch] = d.get(ch,0)+1

#print(d)

for k,v in d.items():

    print(k,'Occurs',v,'Times')


# for sorting
# for k,v in sorted(d.items()):