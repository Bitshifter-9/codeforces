t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    right = [0] * 26
    left = [0] * 26

    for ch in s:
        right[ord(ch) - 97] += 1

    ans = 0
    distinct_left = 0
    distinct_right = sum(1 for x in right if x > 0)

    for i in range(n - 1):
        idx = ord(s[i]) - 97

        # move char from right to left
        if left[idx] == 0:
            distinct_left += 1
        left[idx] += 1

        right[idx] -= 1
        if right[idx] == 0:
            distinct_right -= 1

        ans = max(ans, distinct_left + distinct_right)

    print(ans)
