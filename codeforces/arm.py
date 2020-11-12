num = str(input())
n = len(num)
num = int(num)
ornum = num
sums = 0
d = 0
while(num!=0):
    d = num % 10
    sums += d**n
    num = num//10
if sums == ornum:
    print("YES")
else:
    print("No")
    