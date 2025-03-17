def rem(nums):
    x=set()
    for i in nums:
        x.add(i)
    return len(x)
# n=[0,0,1,1,1,2,2,3,3,4]
n=[1,1,2]
print(rem(n))

# leet code acceptable
def re(nums):
    if not nums:
        return 0
    k=1 #k=0
    for  i in range(1,len(nums)):
        if nums[i] != nums[i-1]: # new element
            nums[k]=nums[i] #add to new position by k
            k+=1
    return k
n=[0,0,1,1,1,2,2,3,3,4]
# n=[1,1,2]
print(rem(n))
