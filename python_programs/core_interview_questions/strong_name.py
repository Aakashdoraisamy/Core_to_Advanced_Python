# 🔹 What is a Strong Number?

# A number is called Strong if the sum of factorials of its digits equals the number itself.

# Example:

# 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✅ Strong

# 123 → 1! + 2! + 3! = 1 + 2 + 6 = 9 ❌ Not Strong


# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# Input range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Strong numbers in range:")

for num in range(start, end+1):
    temp = num
    sum_of_fact = 0
    while temp > 0:
        digit = temp % 10
        sum_of_fact += factorial(digit)
        temp //= 10
    if sum_of_fact == num:
        print(num)
