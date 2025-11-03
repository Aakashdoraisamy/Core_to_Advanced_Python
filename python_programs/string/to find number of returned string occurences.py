s = input("enter any string:")

l = []

for ch in s:

    if ch not in l:

        l.append(ch)

for ch in l:

    print('{} occurs {} number of times'.format(ch,s.count(ch)))








#FOR SORTING THE CHARACTERS

s = input("enter any string:")

l = []

for ch in s:

    if ch not in l:

        l.append(ch)

for ch in sorted(l):

    print('{} occurs {} number of times'.format(ch,s.count(ch)))






#USING SET METHOD

s = input("enter any string:")

s1 = set(s)

for ch in sorted(s1):

    print('{} occurs {} number of times'.format(ch,s.count(ch)))

