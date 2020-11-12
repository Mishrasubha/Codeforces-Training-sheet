n = int(input())
h = []
g = []
num = 0
for i in range(n):
    m = map(int,input().split("\n"))
    h.append(m)
for j in range(n): 
    ni = map(int,input().split("\n"))
    h.append(ni)
for i in range(n):
    for j in range(n):
        if h[j]==g[i]:
            num += 1
        if g[j]==h[i]:
            num+=1
print(num)

