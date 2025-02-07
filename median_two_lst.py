def median(l1, l2):
    x = sorted(l1 + l2)
    n = len(x)
    if n % 2 == 0:
        mid1 = x[n // 2 - 1] 
        mid2 = x[n // 2] 
        return (mid1 + mid2) / 2
    else:
        return x[n // 2]

lst1 = [1,2]
lst2 = [3,4]
print(median(lst1, lst2))  
