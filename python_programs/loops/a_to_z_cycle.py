n = int(input("Enter a number: "))

# 26 letters in alphabet, so we use modulo 26
index = n % 26

result = chr(ord('a') + index)
print(result)
