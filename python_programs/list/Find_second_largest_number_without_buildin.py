lst = [10, 5, 20, 8, 20, 2]

first = second = -999999  # some very small number

for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)


"""
Logic

Initialize two variables:

first = -∞ → largest

second = -∞ → second largest

Traverse the list:

If current number > first:

second = first

first = current number

Else if current number > second and != first:

second = current number


Dry Run

num=10 → first=10, second=-∞

num=5 → second=5

num=20 → first=20, second=10

num=8 → second stays 10

num=20 → first=20, second stays 10

num=2 → second stays 10

Output: Second largest: 10 ✅

"""