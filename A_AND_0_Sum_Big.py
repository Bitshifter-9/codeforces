MOD = 10**9 + 7

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ans = pow(n, k, MOD)
    print(ans-k)
