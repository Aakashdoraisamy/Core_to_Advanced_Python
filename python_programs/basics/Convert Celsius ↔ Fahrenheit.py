# 1st way

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Example usage
c = float(input("Enter temperature in Celsius: "))
print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")

f = float(input("Enter temperature in Fahrenheit: "))
print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")

# Direct way

c = 37
f = (c * 9/5) + 32
print(f"{c}°C = {f}°F")

# 2nd way

choice = int(input("1: Celsius → Fahrenheit\n2: Fahrenheit → Celsius\nChoose: "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")
elif choice == 2:
    f = float(input("Enter Fahrenheit: "))
    print(f"{f}°F = {((f - 32) * 5/9):.2f}°C")
else:
    print("Invalid choice")

# using lambda

c_to_f = lambda c: (c * 9/5) + 32
f_to_c = lambda f: (f - 32) * 5/9
print(c_to_f(37))
print(f_to_c(98.6))
