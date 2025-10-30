t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    

    m=set(lis)
    if len(m)<=1:
        print("NO")
    else:
        y=list(m)
        y.sort(reverse=True)
        w=[]
        for j in range(len(y)):
            q=lis.count(y[j])
            if q>1:
                z=[y[j]]*(q-1)
                w=w+z
        y=y+w
        print("YES")
        print(*y)



