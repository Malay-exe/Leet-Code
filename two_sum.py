def find(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return [i, j]
    return None  

nums = [1,2,3,4,5]
t = 6
result = find(nums, t)

if result:
    print(f"Indices: {result}")
else:
    print("No two digits sum up to the target.")
