t=int(input())
for i  in range(t):
    n,a,b,c,d=map(int,input().split())
    cou=0
    lis=[[0,n+1],[0,0],[n+1,0],[n+1,n+1]]
    arr=[[0,b],[n,b],[a,0],[a,n]]
    ans=-1
    for j in range(4):
        l=abs(a-arr[j][0])+abs(b-arr[j][1])
        m=max(abs(c-arr[j][0]),abs(d-arr[j][1]))
        if m<=l:
            ans=max(ans,1)
        else:
            ans=max(ans,l+(m-l))
    print(ans)