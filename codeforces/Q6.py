n = int(input())
arr = list(map(int,input().split())) 
# arr = [ 2 3 8]
#arr = [ block in column 1,block in column two]
afgrav = []
a = []
for i in range(n):
    a.append(arr[i]) # a = [2 3 8]
    p = a.pop()     # p = [8 3 2]
    afgrav.append(p)    # 8 3 2
afgrav = sorted(afgrav)  #2 3 8

print(*afgrav)


