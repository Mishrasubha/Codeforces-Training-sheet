s = input()
cl = 0
cu = 0
for i in s:
    if i>="A" and i<="Z":
        cu += 1
    if i>="a" and i<="z":
        cl += 1
if cu > cl:
    print(s.upper())
if cl>cu:
    print(s.lower())
elif cl==cu:
    print(s.lower())
    
