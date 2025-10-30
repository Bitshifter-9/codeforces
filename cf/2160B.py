t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    x=[1]
    cou=2
    for j in range(1,n):
        if lis[j]-1==lis[j-1]:
            x.append(1)
        else:
            x.append(cou)
            cou+=1
        # else:
        #     x.append(x[-1])
    print(*x)




