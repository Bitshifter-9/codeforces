n,m=map(int,input().split())
we=True
for i in range(n):
    if i==0  or i%2==0:
        print("#"*m)
    elif we:
        x="."*(m-1)
        print(x+"#")
        we=False
    else:
        x="."*(m-1)
        print("#"+x)
        we=True
