l,b = map(int,input().split())
def whenheavier(l,b):
    y = 0
    if l==b:
        y = 1
    else:
        while(l<b or l==b):
            l *= 3
            b *= 2
            y = y+1
    return y

print(whenheavier(l,b))