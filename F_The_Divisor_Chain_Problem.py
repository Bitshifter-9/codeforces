t=int(input())
for i in range(t):
    n=int(input())
    m=1
    ans=[1]
    s=set()
    for j in range(1,int(n**(0.5))+1):
        if n%j==0:
            s.add(j)
            s.add(n//j)
    while m+m<=n:
        m+=m
        ans.append(m)
    print(ans)