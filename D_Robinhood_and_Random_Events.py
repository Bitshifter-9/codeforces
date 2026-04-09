t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    lis=list(map(int,input().split()))
    j=n
    ans=j
    x=False
    for k in range(n-1,-1,-1):
        if lis[k] != j:
            ans=k+1
            x=True
            break
        j-=1
    an=1
    for op in range(m):
        a,b=map(float,input().split())
        if a>=ans:
            an*=(1-b)
    


    if not x:
        print(float(1.000000))
    else:
       print(1-an)
# 1/4,2/10,4/35,1/6,2/42,4/105
# 3/4,8/10,31/35,5/6,40/42,101/105
# 1,50,28,800/3,70,44,000
# print(0.4057013282%998244353)
  


