t=int(input())
for _ in range(t):
    m=int(input())
    ans=[]
    st=str(m)
    def x(n):
        if n==len(st):
            return 
        ans.append(int(st[n]))
        x(n+1)
    x(0)
    print(*ans)