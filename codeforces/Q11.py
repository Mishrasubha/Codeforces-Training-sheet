n = int(input())
arr = list(map(int,input().split()))
s = 0
d = 0
i = 0
l = n - 1;
a = []
t = 0
while(i<l+1):
    t += 1
    if t%2==0:
        if arr[l] > arr[i]:
            s+=arr[l]
            l -= 1
        else:
            s+=arr[i]
            i+=1
    elif t%2 != 0:
        if arr[l] > arr[i]:
            d+=arr[l]
            l -= 1
        else:
            d+=arr[i]
            i+=1


print(d,s,end=" ")

        