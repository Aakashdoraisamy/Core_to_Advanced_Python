char = input("Enter a character: ")
ascii_value = ord(char)
if ascii_value >= 65 and ascii_value <= 90:
    print(f"{char} is uppercase")
else:
    print(f"{char} is not uppercase")


#2nd way
char = input("Enter a character: ")
if char>= 'A' and char <= 'Z':
    print(f"{char} is uppercase")
elif char >= 'a' and char <= 'z':
    print(f"{char} is not uppercase")
else:
    print("Invalid input")