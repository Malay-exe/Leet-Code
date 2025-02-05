def addi(l1,l2):
    l1[::-1]
    l2[::-1]
    x=int(''.join(map(str,l1)))
    y=int(''.join(map(str,l2)))
    return x+y
lst1=[2,4,3]
lst2=[5,6,4]
print(addi(lst1,lst2))