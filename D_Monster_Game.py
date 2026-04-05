t=int(input())
for op in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    p=[0]*n
    p[0]=b[0]
    i=1
    for i in range(1,n):
        p[i]= p[i-1] + b[i]
    a.sort(reverse=True)
    ans=0
    i=0
    while i < n:
        x=a[i]
        j=i
        while j<n and a[j] == x:
            j += 1
        c=j
        l=0
        r=n - 1
        k=-1
        while l <= r:
            m=(l+r)//2
            if p[m]<=c:
                k=m
                l=m+1
            else:
                r=m-1
        v=(k+1)*x
        if v>ans:
            ans=v
        i=j
    print(ans)
