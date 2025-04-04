def removeElement(nums, val):
    k = 0  
    for num in nums:
        if num != val:
            nums[k] = num  
            k += 1  
    return k
print(removeElement([1,2,2,3,4,5,4,3],2))