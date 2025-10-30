t = int(input())
for _ in range(t):
    n = int(input())
    b = []
    ma = []
    for _ in range(n):
        d = list(map(int, input().split()))
        k = d[0]
        b.append(d[1:])
        ma.append(k)

    pl = list(range(n))
    rs = []
    cc = 0

    while pl:
        if len(pl) == 1:
            i = pl[0]
            rs.extend(b[i][cc:])
            break

        cd = pl[:]
        c = cc
        while len(cd) > 1:
            mv = float('inf')
            nc = []
            for i in cd:
                if c < ma[i]:
                    v = b[i][c]
                    if v < mv:
                        mv = v
                        nc = [i]
                    elif v == mv:
                        nc.append(i)
            if not nc:
                break
            cd = nc
            c += 1

        i = cd[0]
        rs.extend(b[i][cc:])
        cc = ma[i]

        new_pl = []
        for x in pl:
            if x != i and ma[x] > cc:
                new_pl.append(x)
        pl.clear()
        pl.extend(new_pl)

    print(*rs)
