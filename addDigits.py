def count(num):
    x=0
    c=0
    while num>0:
        num=num//10
        c+=1
    return c
# print(count(12345))
def Add_Digits(nums):
    x=0
    y=0
    while nums>0:
        x=nums%10
        y+=x
        nums//=10
    # print(y)
    if count(y)==1:
        return y
    else:
        return Add_Digits(y)
print(Add_Digits(348))