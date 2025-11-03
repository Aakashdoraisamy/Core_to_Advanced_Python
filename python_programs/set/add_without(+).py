s = {1, 2, 3}
new = {int(input("Enter your value to add: "))}  # take input and make it a set
s = s | new   # use union instead of add() method 
print(s)