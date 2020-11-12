n = int(input())
arr = list(map(int,input().split()))
c  = 0
u = 0
for i in range(n):
    if arr[i]>0:
        c += arr[i]
    else:
        if c<1:
            u += 1
        else:
            c -= 1
print(u)