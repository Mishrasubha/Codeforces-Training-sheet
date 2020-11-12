n , h = map(int,input().split())
arr = list(map(int,input().split()))
def findwidth(n,h,arr):
    w = 0
    for i in range(n):
        if arr[i] > h:
            w = w+2
        else:
            w = w+1
    return w
print(findwidth(n,h,arr))
