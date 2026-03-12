t=int(input())
for i in range(t):
    n,h,k=map(int,input().split())
    lis=list(map(int,input().split()))
    suf=[]
    su=0
    pre_max=float("-inf")
    ma=[0]*n
    for j in lis:
        su+=j
        suf.append(su)
    for _ in range(n-1,-1,-1):
        pre_max=max(pre_max,lis[_])
        ma[_]=pre_max
    to=suf[-1]
    mi_n=[float("inf")]*(n+1)
    for io in range(n):
        mi_n[io+1]=min(mi_n[io],lis[io])
    be=[0]*(n+1)
    for by in range(1,n+1):
        if by<n:
            q=max(0,ma[by]-mi_n[by])
            be[by]=suf[by-1]+q
        else:
            q=max(0,0-mi_n[by])
            be[by]=suf[by-1]+q    
    z=(h-1)//to
    ans = z * (n + k)
    rem = h - z * to
    ind=-1
    for op in range(1,n+1):
        if be[op]>=rem:
            ind=op
            break

    print(ans+ind)

    
    

