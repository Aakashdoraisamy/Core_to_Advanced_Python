# CHECKS IF THE LAST DIGIT OF A NUMBER IS 5 OR NOT

num = int(input("Enter an integer: "))
digit = num % 10
if digit == 5:
    print("Batman")
else:
    print("The last digit is:", digit)