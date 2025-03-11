def con_438(s):
    while True:
        new_s = ""
        for i in range(len(s) - 1):
            new_s += str((int(s[i]) + int(s[i+1])) % 10)
            print(new_s)
        
        if len(new_s) == 1:
            return False
        elif len(set(new_s)) == 1:
            return True
        else:
            s = new_s

# Example usage
# s = "34789"
s="3902"
print(con_438(s))
