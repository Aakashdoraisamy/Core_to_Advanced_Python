s = input("enter a string value:")

i = 0

while i < len(s):

    print(s[i],end = '')

    i = i+2

print(" :the character present at even")

i = 1

while i < len(s):

    print(s[i],end = '')

    i = i+2

print(" :the character present at odd")

		# (OR)

s = input("enter a string value:")

print("the character present at even index :",s[0::2])

print("the character present at odd index :",s[1::2])