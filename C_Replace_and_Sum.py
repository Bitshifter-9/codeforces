t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for j in range(n):
        if b[j]>a[j]:
            a[j]=b[j]
    for k in range(n-2, -1, -1):
        a[k] = max(a[k], a[k+1])

    pre=[0]
    ad=0
    for np in range(n):
        ad+=a[np]
        pre.append(ad)
    arr=[]
    for  op in range(q):
        l,r=map(int,input().split())
        arr.append(pre[r]-pre[l-1])
    print(*arr)
    # print(a)

