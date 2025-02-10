def sti(st):
    x=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    y=[]
    for  i in range(0,len(st)):
       if st[i] not in x:
            y.append(st[i])
            a=int(''.join(map(str,y)))
    return a        
st="123aasf"
print(sti(st))