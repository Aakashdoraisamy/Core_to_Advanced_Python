num = int(input('Enter a number:'))
even_count , odd_count , even_sum , odd_sum = 0,0,0,0
while num > 0:  
# (0r) != 0:
    r = num % 10
    if r % 2 == 0:
        even_count += 1
        even_sum += r
    else:
        odd_count += 1
        odd_sum += r
    num = num // 10
print(f'Count of even numbers is {even_count} and Sum of even numbers is {even_sum} and Average of even numbers is {even_sum/even_count if even_count > 0 else 0}')
print(f'Count of odd numbers is {odd_count} and Sum of odd numbers is {odd_sum} and Average of odd numbers is {odd_sum/odd_count if odd_count > 0 else 0}')