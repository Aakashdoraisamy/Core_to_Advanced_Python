a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b

while y != 0:
    temp = y
    y = x % y
    x = temp

gcd = x
print("GCD:", gcd)


# LCM

lcm = (a * b) // gcd
print("LCM:", lcm)

"""
🔹 1. GCD (Greatest Common Divisor)

Definition:
The largest number that divides both numbers exactly.

Logic (Euclidean Algorithm):

Take two numbers, a and b.

While the second number (b) is not 0:

Replace a with b

Replace b with a % b (remainder when a is divided by b)

When b becomes 0, the remaining a is the GCD.

Step Example:

Numbers: 12 and 18

Step 1: 18 % 12 = 6 → new numbers: 12, 6

Step 2: 12 % 6 = 0 → new numbers: 6, 0

Stop → GCD = 6 ✅

Why it works:

Repeatedly replacing numbers with (smaller number, remainder) reduces the problem until the remainder is 0.

The last non-zero remainder divides both numbers exactly.

🔹 2. LCM (Least Common Multiple)

Definition:
The smallest number divisible by both numbers.

Logic:

LCM
×
GCD
=
𝑎
×
𝑏
LCM×GCD=a×b

So, after finding GCD, we can calculate:

LCM
=
𝑎
×
𝑏
GCD
LCM=
GCD
a×b
	​


Step Example:

Numbers: 12 and 18

GCD = 6

LCM = (12 × 18) / 6 = 216 / 6 = 36 ✅

Why it works:

Multiplying the numbers gives a number divisible by both.

Dividing by GCD removes the common factors, giving the smallest multiple.

🔹 Summary Logic

GCD: Use Euclidean algorithm → reduce numbers using remainder until second number is 0.

LCM: Multiply the numbers and divide by GCD.

"""