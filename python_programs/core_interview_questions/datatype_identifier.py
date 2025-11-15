data_types = ["int", "float", "str", "bool", "list", "tuple", "set", "dict"]

user_input = input("Enter something: ")

value = eval(user_input)

# get type name (allowed because it's not a function used for checking)
t = type(value).__name__

if t in data_types:
    if t in ["int", "float", "str", "bool"]:
        print(t, "→ Primitive Data Type")
    else:
        print(t, "→ Non-Primitive Data Type")
else:
    print("Unknown data type")


x = eval(input("Enter: "))
if type(x) == int or type(x) == float or type(x) == bool or type(x) == str:
    print("Primitive")
else:
    print("Non-Primitive")
