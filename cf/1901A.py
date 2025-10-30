def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    pref = 0
    freq = {0: 1}   # store counts of prefix % k
    ans = 0

    for x in arr:
        if x % k == 0:
            pref += 1
        mod_val = pref % k
        if mod_val in freq:
            ans += freq[mod_val]
            freq[mod_val] += 1
        else:
            freq[mod_val] = 1

    print(ans)
solve()