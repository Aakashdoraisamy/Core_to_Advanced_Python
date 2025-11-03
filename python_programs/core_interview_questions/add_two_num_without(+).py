# write a program to sum the two numbers without using + operator

a = int(input('Enter first number:')) # 7
b = int(input('enter Second number:')) # 5
l1 = '0' * a # '0000000'
l2 = '1' * b # '11111'
print(len(f'{l1}{l2}')) # '000000011111' # 12