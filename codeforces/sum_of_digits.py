s = input()
ans = 0
while int(s) >= 10:
	count = 0
	for c in s:
		count += int(c)
	s = str(count)
	ans += 1
 
print(ans)
