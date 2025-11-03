def moveZeroes(nums):
    a = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[a] = nums[a],nums[i]
            a+=1
    return nums
print(moveZeroes([1,2,3,0,1,2]))