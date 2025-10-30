t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    x=[lis[0]]
    cou=0
    for j in range(1,n):
        if x[-1]%2==lis[j]%2:
            x[-1]=x[-1]*lis[j]
            cou+=1
        else:
            x.append(lis[j])
    print(cou)

