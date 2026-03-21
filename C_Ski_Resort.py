t=int(input())
for i in range(t):
    n,k,q=map(int,input().split())
    lis=list(map(int,input().split()))
    x=[]
    cou=0
    ans=True
    for j in range(n):
        if lis[j]<=q:
            cou+=1
            ans=True
        else:
            if ans:
                x.append(cou)
                cou=0
                ans=False
    x.append(cou)
    su=0
    # print(x)
    for l in range(len(x)):
        if x[l]>=k:
            su+= ((x[l]-k+1)*(x[l]-k+2))//2
    print(su)


