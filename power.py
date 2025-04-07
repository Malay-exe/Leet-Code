def pow(x,n):
    if x==0:
            return 0
    elif x>0:
        print("nok")
        return x**n
    elif x<0 and n<0:
        print("ok")
        return (1/(x**abs(n)))
    elif n<0:
        return (1/(x**n))
    return (x**n)
print(pow(-3,-5))