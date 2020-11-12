t = int(input())
while(t>0):
    p = list(map(int,input().split()))
    a = p[0]
    b = p[1]
    c = p[2]
    d = p[3]
    print(max(a+b,c+d))
    t -= 1