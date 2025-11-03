number = int(input("enter any positive number:"))
for i in range(2,number):
    if number % i == 0:
        print("it is not prime number")
        break
else:
        print("it is prime number")
        
prime = int(input("Enter a number: "))
if prime%3 == 0 or prime%7 == 0:
    print(f"{prime} is a Divisible by 3 and 7")
else:
    print(f"{prime} is not Divisible by 3 and 7")