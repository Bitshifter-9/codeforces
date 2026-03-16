from collections import deque

def sl(nk, kk):
    if nk == kk:
        return 0
    if kk > nk:
        return -1

    qu = deque([(nk, 0)])
    vs = {nk}

    while qu:
        sz, st = qu.popleft()
        lf = sz // 2
        rt = (sz + 1) // 2

        if lf == kk or rt == kk:
            return st + 1

        for ns in (lf, rt):
            if ns >= kk and ns not in vs:
                vs.add(ns)
                qu.append((ns, st + 1))

    return -1

tt = int(input())
for _ in range(tt):
    nn, kk = map(int, input().split())
    print(sl(nn, kk))

