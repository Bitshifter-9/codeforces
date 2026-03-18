import math
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    lis=list(map(int,input().split()))
    mi=float("inf")
    cou_eve=0
    for j in range(n):
        x=math.ceil(lis[j]/k)
        mi=min(mi,k*x-(lis[j]))
        if lis[j]%2==0:
            cou_eve+=1
    if k==4:
        if cou_eve>=2:
            print(min(mi,0))
        elif cou_eve==1:
            print(min(mi,1))
        else:
            print(min(mi,2))
    else:
        print(mi)