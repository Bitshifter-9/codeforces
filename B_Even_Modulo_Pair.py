t=int(input())

for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))

    ans=False
    arr=[]

    for j in range(min(n,1000)):
        if ans:
            break

        for k in range(j+1,min(n,1000)):
            x = lis[k]%lis[j]
            if x%2==0:
                ans=True
                print(lis[j],lis[k])
                break

    if not ans:
        print(-1)