num = int(input("Enter a number: "))
if (num >= 0 and num <= 9) or (num >= -9 and num <= 0): 
    print(f"{num} is a single digit number")
elif (num >= 10 and num <= 99) or (num >= -99 and num <= -10): 
    print(f"{num} is a double digit number")
elif num >= 100 and num <= 999 or (num >= -999 and num <= -100):
    print(f"{num} is a triple digit number")
else:
    print("Invalid input") 