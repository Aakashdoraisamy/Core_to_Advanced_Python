def remove(nums,val):
    p = 0
    for i in range(0,len(nums)):
        if nums[i] == val:
            continue
        else:
            nums[p] = nums[i]
            p+=1
    return p
print(remove([3,2,2,3], 3))