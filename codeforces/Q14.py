arcal = list(map(int,input().split())) #[1 5 3 2]
s = input()
ccal = []
sumc = 0
for i in s:
    ccal.append(int(i))
#ccal = ccal.sort() # 1 1 1 2 2
#for i in range(len(ccal)):
#print(ccal)
for i in range(len(ccal)):
    if ccal[i] == 1:
        sumc = sumc + arcal[0]
    elif ccal[i] == 2:
        sumc = sumc + arcal[1]
    elif ccal[i] == 3:
        sumc = sumc + arcal[2]
    elif ccal[i] == 4:
        sumc = sumc + arcal[3]
print(sumc)
