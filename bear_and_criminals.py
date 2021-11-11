def main():  
    n,a = map(int,input().split())
    city = list(map(int,input().split()))
    c = 0
    i = a-1
    j = a+1
    if city[a]==1:
        c+=1
    while(i>=1 and j<=n):
        if city[i]==1 and city[j]==1:
            c = c+2
        elif i>=1:
            c+=1
        elif j<=n:
            c+=1
        i-=1
        j+=1
    print(c)
 
 
if __name__ == '__main__':
    main()
