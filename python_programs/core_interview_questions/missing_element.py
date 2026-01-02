nums = list(range(1, 101))
nums.remove(57)  

n = 100
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print("Missing number:", missing)
