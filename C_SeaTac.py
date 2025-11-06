import sys
sys.setrecursionlimit(10**6)

n, m, g = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[b - 1].append(a)

q = []
vis = [0] * n
ans = []

def dfs(i):
    q.append(i)
    if i == 1:
        ans.append(q[:])
    else:
        for j in arr[i - 1]:
            if not vis[j - 1]:
                vis[j - 1] = 1
                dfs(j)
                vis[j - 1] = 0
    q.pop()   # ✅ now matches the append

dfs(n)

mx = float("inf")
for path in ans:
    mx = min(mx, (len(path) - 1) % g)
print(mx)
