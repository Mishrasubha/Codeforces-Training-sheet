t = int(input())
while(t>0):
    p , q = map(int,input().split())
    for i in range(1,p+1):
        if p%i==0 and i%q!=0:
            a = i
            continue
    print(a)
    t -= 1