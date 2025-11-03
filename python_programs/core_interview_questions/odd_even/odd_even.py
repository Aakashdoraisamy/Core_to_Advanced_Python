num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   
   
# using division
   
n = int(input("Enter a number: "))

if (n // 2) * 2 == n:
    print("Even")
else:
    print("Odd")
    
# Using Ternary Operator (One-liner)

n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")


# using function

def check_odd_even(n):
    return "Even" if n % 2 == 0 else "Odd"

n = int(input("Enter a number: "))
print(check_odd_even(n))
