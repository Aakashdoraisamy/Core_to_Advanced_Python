from datetime import datetime

number = int(input("Enter a number: "))

# Check odd or even
if number % 2 == 0:
    result = "Even"
    print("The number is Even.")
else:
    result = "Odd"
    print("The number is Odd.")

# Current date & time
timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Save to file
with open("odd_even_log.txt", "a") as file:
    file.write(f"Number: {number} | Result: {result} | Time: {timestamp}\n")

print("Result saved successfully!")
