t=int(input())
for j in range(t):
    x,m=map(int,input().split())
    i=1
    ans=0
    se=set()
    while i<=min(2*x,m):
        if i!=x:
            ok=i^x
            if i%ok==0 or x%ok==0:
                ans+=1
        i+=1
    print(ans)