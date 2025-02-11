import string

def sti(st):
    y = []
    for char in st:
        if char not in string.ascii_lowercase:  
            y.append(char)  
            a=int(''.join(map(str,y)))
    return a 

st = "a123"
print(sti(st))
