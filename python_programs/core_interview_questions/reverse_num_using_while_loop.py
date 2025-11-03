n = int(input('enter a Number:'))
while n>0:
    rem = n%10
    print(rem, end=' ')
    n = n//10
    
num = int(input('Enter a number:'))
rev = 0
while num>0:
    r = num%10
    rev = rev*10 + r
    num = num//10
print(f'Reversed number is {rev}')