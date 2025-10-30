t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    cou=0
    ans=0
    for j in range(n):
        if lis[j]==0:
            cou+=1
        else:
            ans=max(cou,ans)
            cou=0
    ans=max(cou,ans)
    print(ans)
