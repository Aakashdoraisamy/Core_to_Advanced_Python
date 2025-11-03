def is_perfect(num):
    total = 0
    
    for i in range(1,num):

        if num%i == 0:
            total+=i

    return total == num

perfect_numbers = []

for j in range(1,10001):

    if is_perfect(j):
        perfect_numbers.append(j)

print(perfect_numbers)  # [6, 28, 496, 8128]
is_perfect(6)  # True
