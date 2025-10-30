t=int(input())
for i in range(t):
    n,k,x=map(int,input().split())
    cou=0
    su=0
    ma=n
    p=(k*(k+1))//2
    z=n-k
    m=((n*(n+1))//2)-((z*(z+1))//2)
    if x<=m and x>=p:
        print("YES")
    else:
        print("NO")