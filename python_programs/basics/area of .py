# 1. Circle

import math

r = float(input("Enter radius of circle: "))
area = math.pi * r * r
perimeter = 2 * math.pi * r
print(f"Circle → Area = {area:.2f}, Perimeter = {perimeter:.2f}")

# 2. Square

import math

side = float(input("Enter side of square: "))
area = side * side
perimeter = 4 * side
print(f"Square → Area = {area}, Perimeter = {perimeter}")

# 3. Rectangle

# Area = length × breadth

# Perimeter = 2 × (length + breadth)

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Rectangle → Area = {area}, Perimeter = {perimeter}")


# 4. Triangle

# Area (Heron’s Formula) = √[s(s-a)(s-b)(s-c)]
# where s = (a+b+c)/2 (semi-perimeter)

# Perimeter = a + b + c

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

perimeter = a + b + c
s = perimeter / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Triangle → Area = {area:.2f}, Perimeter = {perimeter}")


### 5. Menu-driven program for all shapes

import math

print("1. Circle\n2. Square\n3. Rectangle\n4. Triangle")
choice = int(input("Choose a shape: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print(f"Area = {math.pi * r * r:.2f}, Perimeter = {2 * math.pi * r:.2f}")

elif choice == 2:
    side = float(input("Enter side: "))
    print(f"Area = {side * side}, Perimeter = {4 * side}")

elif choice == 3:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print(f"Area = {l * b}, Perimeter = {2 * (l + b)}")

elif choice == 4:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Area = {area:.2f}, Perimeter = {a + b + c}")

else:
    print("Invalid choice")

