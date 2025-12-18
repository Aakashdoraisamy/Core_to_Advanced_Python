num = input('Enter your number:')
sum = 0 
for i in num:
    sum+=int(i)**3
if sum == int(num):
    print(f'{num} is amstrong number')
else:
    print(f"{num} is not amstrong number")






















# num = input("Enter a number: ")
# sum_of_powers = sum(int(digit) ** len(num) for digit in num)

# if sum_of_powers == int(num):
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")


# n = int(input('enter the number:'))
# num = n
# s = 0
# while n>0:
#     r = n%10
#     s = s+r*r*r
#     n = n//10
# if s == num:
#     print(num,"it is amstrong")
# else:
#     print(num,"it is not amstrong")
    
# """
    
#     🔹 Step-by-Step Explanation
# 1️⃣ Take Input
# n = int(input('enter the number:'))


# User enters a number (e.g., 153).

# Stored as integer n.

# 2️⃣ Store Original Number
# num = n


# We save the original number in num.

# This is because we will change n in the loop.

# 3️⃣ Initialize Sum
# s = 0


# s will store the sum of cubes of digits.

# Initially 0.

# 4️⃣ Loop Through Digits
# while n > 0:


# Loop runs until all digits of n are processed.

# Example: n = 153 → loop will run 3 times.

# Inside the loop:

# Get last digit

# r = n % 10


# % 10 gives the last digit.

# Example: 153 % 10 = 3 → r = 3

# Add cube of digit to sum

# s = s + r*r*r


# Cube the digit and add to sum.

# Example: s = 0 + 3*3*3 = 27

# Remove last digit from n

# n = n // 10


# // 10 removes last digit.

# Example: 153 // 10 = 15 → next iteration

# 5️⃣ Check if Armstrong
# if s == num:
#     print(num,"it is amstrong")
# else:
#     print(num,"it is not amstrong")


# Compare the sum of cubes (s) with the original number (num).

# If equal → Armstrong number

# Else → Not Armstrong

# 🔹 Dry Run Example (153)
# Step	n	r (n%10)	s (sum of cubes)	n after //10
# 1	153	3	27	15
# 2	15	5	27 + 125 = 152	1
# 3	1	1	152 + 1 = 153	0

# s = 153, num = 153 → Armstrong ✅

# """