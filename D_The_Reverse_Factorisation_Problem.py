t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    lis.sort()
    ans=lis[0]*lis[-1]
    j=2
    se=set()
    while j*j<=ans:
        if ans%j==0:
            se.add(j)
            if j!=ans//j:
                se.add(ans//j)
        j+=1
    if set(lis)==se:
        print(ans)
    else:
        print(-1)
    





        