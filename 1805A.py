t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    l=lis[0]
    for j in range(1,n):
        l=l^lis[j]
    for k in range(n):
        lis[k]=lis[k]^l
    q=lis[0]
    for m in range(1,n):
        q=q^lis[m]
    if q==0:
        print(l)
    else:
        print(-1)
 