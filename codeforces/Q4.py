n = int(input())
c = 0
while(n!=0):
    p,v,t = map(int,input().split())
    if p==1 and v==1 or p==1 and t==1 or v==1 and t==1 or p==1 and v==1 and t==1:
        c+=1
    n = n-1
print(c)