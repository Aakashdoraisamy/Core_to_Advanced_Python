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