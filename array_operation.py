def l(nums):
        x=[]
        z=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for j in nums:
            if j>0:
                x.append(j)
            else:
                z.append(j)
        return x+z
n=[1,2,2,1,1,1,0]
# n=[1,0]
print(l(n))