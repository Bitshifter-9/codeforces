t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    a=lis[0]
    for j in lis:
        a=a&j
    print(a)