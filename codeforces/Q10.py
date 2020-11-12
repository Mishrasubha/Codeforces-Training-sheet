n = int(input())
arr = []
g = 1
for i in range(n):
    m = int(input())
    arr.append(m)
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        g += 1
print(g)
    
