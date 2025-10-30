t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    ans="No"
    for j in range(max(lis),0,-1):
        cou=0
        for k in range(n):
            if lis[k]%j==0:
                cou+=1
        if cou==n:
            if j<=n:
                ans="Yes"
                print(j)
            break
    print(ans)


