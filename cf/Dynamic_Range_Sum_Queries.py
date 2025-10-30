import math

n, q = map(int, input().split())
lis = list(map(int, input().split()))
root = int(math.sqrt(n)) + 1
a = [0] * root  
for i in range(n):
    a[i // root] += lis[i]

for _ in range(q):
    num, k, u = input().split()
    k = int(k)
    u = int(u)
    if num == "1":  
        idx = k - 1
        block_idx = idx // root
        a[block_idx] += u - lis[idx]
        lis[idx] = u
    else:  
        l = k - 1
        r = u - 1
        su_m = 0
        while l <= r and l % root != 0:
            su_m += lis[l]
            l += 1
        while l + root - 1 <= r:
            su_m += a[l // root]
            l += root
        while l <= r:
            su_m += lis[l]
            l += 1
        print(su_m)

