def searchInsert( nums, target):
        for i in range(len(nums)):
                if target == nums[i]: 
                    return i
                elif target < nums[i]:  
                    return i
        return len(nums)
# x=[3,6,7,8,10]
# x=[1002]
x=[1,2,3,4]
print(searchInsert(x,6))