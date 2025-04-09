def single(nums):
    c={}
    for i in nums:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    for i in c:
        if c[i]==1:
            return i
x=[1,1,2,3,3,4,6,5]
print(single(x))