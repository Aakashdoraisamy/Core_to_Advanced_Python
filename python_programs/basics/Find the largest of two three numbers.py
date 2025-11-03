# Method 1: Using if-else

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(f"Largest = {a}")
else:
    print(f"Largest = {b}")

# Method 2: Using Ternary Operator (short form)

a = 10
b = 20
largest = a if a > b else b
print("Largest =", largest)

# Method 3: Using max() (built-in)

a = 10
b = 20
print("Largest =", max(a, b))

# 2. Largest of Three Numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"Largest = {a}")
elif b >= a and b >= c:
    print(f"Largest = {b}")
else:
    print(f"Largest = {c}")

# Method 2: Using Nested if

a, b, c = 10, 25, 15

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print("Largest =", largest)


# Method 3: Using max()

a, b, c = 10, 25, 15
print("Largest =", max(a, b, c))
