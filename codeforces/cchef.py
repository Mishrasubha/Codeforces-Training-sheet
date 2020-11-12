def findx(a,b):
    for i in range(1,a+1):
        if a%i == 0 and i %b != 0:
            r = i
            continue
    return r
if __name__ == "__main__":
    t = int(input())
    while(t!=0):
        p,q = map(int,input().split())
        
        t -= 1
        print(findx(p,q))