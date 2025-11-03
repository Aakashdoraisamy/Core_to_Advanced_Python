user = int(input('Enter a number:'))
total = 0
for i in range(1,user+1):
    total+=int(input(f'Enter number {i}:'))
print(f'Sum is {total} and Average is {total/user}')