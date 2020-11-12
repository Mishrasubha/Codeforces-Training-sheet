s = input()
st = "a"
n = len(s)
l1 = 0
l2 = 0
sumd = 0
for i in range(n):
    l1 = abs(ord(s[i])-ord(st))
    l2 = 26 - abs(ord(s[i])-ord(st))
    sumd += min(l1,l2)
    st = s[i]

print(sumd)