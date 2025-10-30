t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    if n==1:
        print(0)
        continue
    ans=float("-inf")
    for k in  range(1,n):
        ans=max(ans,lis[k]-lis[0])
    for j in range(n-1):
        ans=max(ans,lis[-1]-lis[j])
    for m in range(n-1):
        ans=max(ans,lis[m]-lis[m+1])
    ans=max(ans,lis[-1]-lis[0])
    print(ans)
