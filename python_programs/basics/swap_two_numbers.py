a = 10
b = 20
a,b = b,a
print(a)
print(b)

a=(input("enter the value:"))
b=(input("enter the value:"))
print(f"values before swapping:{a} and {b}")
temp=a
a=b
b=temp
print(f"values after swapping:{a} and {b}")