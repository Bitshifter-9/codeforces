t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    x = int(input())
    o = False
    if n==1:
        if lis[0]==x:
            print("YES")
        else:
            print("NO")
    else:
        if min(lis)<=x<=max(lis):
            print("YES")
        else:
            print("NO")



