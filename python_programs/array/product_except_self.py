# USING DIVIDE
# TIME COMPLEXITY O(N)
# SPACE COMPLEXITY O(N)

def productExceptSelf(nums):
    total_product = 1
    for num in nums:
        total_product *= num   # multiply everything together

    result = []
    for num in nums:
        result.append(total_product // num)  # divide total by current element
    return result
print(productExceptSelf([1,2,3,4]))

# WITHOUT DIVISION

def productExceptSelf(nums):
    final = [1]*len(nums)
    pre = 1
    for i in range(len(nums)):
        final[i] = pre
        pre = pre*nums[i]
    suf = 1
    for i in range(len(nums)-1,-1,-1):
        final[i] = final[i]*suf
        suf = suf*nums[i]
    return final
print(productExceptSelf([1,2,3,4]))
        
