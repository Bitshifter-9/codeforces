import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()                  # ascending
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + a[i]

    dp = [10**30] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        # buy item i normally
        dp[i] = dp[i-1] + a[i-1]

        if i >= k + 1:
            block_sum = pref[i] - pref[i-(k+1)]
            smallest_in_block = a[i-(k+1)]
            cost_block = block_sum - smallest_in_block
            dp[i] = min(dp[i], dp[i-(k+1)] + cost_block)

    print(*dp[1:])
