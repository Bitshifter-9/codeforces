t=int(input())
for i in range(t):
    d = list(map(int, input().split()))
    n = d[0]
    m = d[1]
    p = 0
    s = 0
    a = 0
    for _ in range(n):
        x, y = map(int, input().split())
        l = x - p
        if l % 2 == s ^ y:
            a += l
        else:
            a += l - 1
        p = x
        s = y
    a += m - p
    print(a)
