n = int(input())
s = input()
def whowon(n,s):
    ca = 0
    cd = 0
    for i in s:
        if i =="A":
            ca += 1
        else:
            cd += 1
    if ca>cd:
        return "Anton"
    if ca==cd:
        return "Friendship"
    else:
        return "Danik"
print(whowon(n,s))