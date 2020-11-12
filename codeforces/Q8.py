s = input()
arr = []
for i in range(len(s)):
    a = s[i]
    if a not in arr:
        arr.append(a)
if len(arr) % 2 ==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")