for _ in range(int(input())):
    n = int(input())
    k = 2
    while 1:
        x = (2 ** k) - 1
        if n % x == 0:
            print(n // x)
            break
        k += 1