t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    lis.sort()
    ans=float("-inf")
    for j in range(n-1):
        if j%2==0:
            ans=max(ans,abs(lis[j]-lis[j+1]))
    print(ans)