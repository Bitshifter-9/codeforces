m=300000
spf=list(range(m+1))
for i in range(2,m+1):
    if spf[i]==i:
        for j in range(i*i,m+1,i):
            if spf[j]==j:
                spf[j]=i
def div(x):
    di=[1]
    while x > 1:
        p=spf[x]
        cnt=0
        while x%p== 0:
            x//=p
            cnt+=1
        ab=di
        m=1
        ne=[]
        for _ in range(cnt):
            m*=p
            for d in ab:
                ne.append(d * m)
        di=ab+ne
    return di
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    p=[0]*(n+1)
    for v in a:
        p[v]=1
    dp=[float("inf")] * (n + 1)
    dp[1]=0
    for i in range(2, n + 1):
        b=float("inf")
        divs=div(i)
        # print(divs)
        for d in divs:
            if d<=n and p[d]:
                pr=i//d
                if dp[pr]!= float("inf"):
                    b = min(b,dp[pr]+1)
        dp[i]=b
    ans=[]
    for i in range(1,n+1):
        if i==1:
            if p[1]:
                ans.append(1)
            else:
                ans.append(-1)
        else:
            if dp[i]==float("inf"):
                ans.append(-1)
            else:
                ans.append(dp[i])
    print(*ans)
