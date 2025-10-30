t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    vis=[0]*(n+1)
    lis=list(map(int,input().split()))
    ans=lis.count(k)
    cou=0
    lis.sort()
    for j in range(n):
        vis[lis[j]]=1
    for j in range(n):
        if vis[j]==0 and j!=k and j<k:
            cou+=1
    if cou<ans:
        print(ans)
    else:
        print(ans+(cou-ans))

    # print(ans,vis)