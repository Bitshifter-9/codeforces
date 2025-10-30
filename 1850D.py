t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    lis=list(map(int,input().split()))
    lis.sort()
    le=0
    cou=1
    for j in range(n-1):
        if lis[j+1]-lis[j]<=k:
            cou+=1
        else:
            le=max(cou,le)
            cou=1
    le=max(cou,le)
    print(abs(le-n))