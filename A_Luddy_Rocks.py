t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    d = {'Y': 1, 'L': 1, 'R': 1, 'D': 2, 'O': 1, 'U': 1, 'C': 1, 'S': 1, 'K': 1}
    ans = True
    for i in s:
        if i in d:
            d[i] -= 1
    for i in d:
        if d[i] >= 1:
            ans = False
    if ans:
        print("YES")
    else:
        print("NO")