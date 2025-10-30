t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    mi_n=-1
    if sorted(lis)!=lis:
        print(0)
    else:

        for j in range(n-1):
            x=(lis[j+1]-lis[j])//2
            if mi_n==-1:
                mi_n=x+1
            else:
                mi_n=min(mi_n,x+1)
        print(mi_n)

