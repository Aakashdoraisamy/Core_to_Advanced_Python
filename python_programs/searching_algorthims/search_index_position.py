def func(nums,target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)
print(func([1,3,5,6],4))