num = int(input('Enter a Number:'))
if num%7 == 0:
    if num%4 == 0:
        print(f'{num} is divisible by 7 and 4')
    else:
        print(f'{num} is divisible by 7 but not by 4')
else:
    if num%4 == 0:
        print(f'{num} is not divisible by 7 but divisible by 4')
    else:
        print(f'{num} is not divisible by 7 and 4')