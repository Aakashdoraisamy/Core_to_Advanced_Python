a = ['Even','Odd']
print(f'the entered value is : {a[int(input("enter Your Number:"))%2]}')


"""
# explaination

Step 1: a = ['Even', 'Odd']
a[0] = even
a[1] = odd

Step 2: int(input("enter Your Number:"))

Step 3: n % 2
% is modulus (remainder).
If n is even, n % 2 = 0.
If n is odd, n % 2 = 1.

Step 4: a[n % 2]
If remainder is 0 → a[0] → 'Even'
If remainder is 1 → a[1] → 'Odd'

"""