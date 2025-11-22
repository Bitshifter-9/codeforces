t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = 2
    g = []
    for i in range(n):
        val = m * (i + 1) - arr[i]
        g.append(val)

    mx = 0
    cur = 0
    for x in g:
        cur += x
        if cur < 0:
            cur = 0
        if cur > mx:
            mx = cur

    print(sum(arr) + mx)
