def perfect_number(n):
    sum_divisors = 0
    divisors = []  

    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
            divisors.append(i)

    print(f"Divisors of {n} (excluding itself): {divisors}")
    
    if sum_divisors == n:
        print(f"{n} is a Perfect Number")
    else:
        print(f"{n} is NOT a Perfect Number")

perfect_number(int(input('enter Your number:')))