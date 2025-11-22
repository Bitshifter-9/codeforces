t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    # if lis[-1]==lis[0] and lis[0]==-1:
    #      continue
    if lis[-1]==-1 and lis[0]!=-1:
        lis[-1]=lis[0]
    elif  lis[0]==-1 and lis[-1]!=-1:
        lis[0]=lis[-1]
    for j in range(n):
            if lis[j]==-1:
                lis[j]=0
    cou=0
    for k in range(n-1):
        cou+=(lis[k+1]-lis[k])
        print(cou)
    print(abs(cou))
    print(*lis)