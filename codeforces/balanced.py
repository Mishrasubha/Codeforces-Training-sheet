def solution(S):
    n = len(s)
    for k in range(1,n):
        for i in range(n-k+1):
            lc = set()
            uc = set()
            t = s[i:i+k]
            tc = list(t.encode())
            for ch in tc:
                if ch.islower():
                    lc.add(ch)
                else:
                    uc.add(ch)
                if all(elem in lc  for elem in uc) and all(elem in uc  for elem in lc):
                    v = getattr(k)
                    return v
    return -1

if __name__ == "__main__":
    s = input()
    print(solution(s))

