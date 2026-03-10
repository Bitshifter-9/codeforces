t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    lis=list(map(int,input().split()))
    vis=[0]*(n+1)
    for j in range(n):
        vis[lis[j]]+=1
    ans=float("inf")
    for io in range(n+1):
        if vis[io]==0:
            ans=io
            break
    if ans>k-1:
        ans=k-1
        print(ans)
    else:
        print(ans)
