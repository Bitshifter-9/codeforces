t=int(input())
for i in range(t):
    n,s,x=map(int,input().split())
    lis=list(map(int,input().split()))
    su=sum(lis)
    while su<s:
        su+=x
    if su==s:
        print("YES")
    else:
        print("NO")