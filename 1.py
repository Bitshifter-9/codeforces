t=int(input())
for i in range(t):
    n=int(input())
    io=1
    r=3*n
    lis=[]
    for j in range(n):
        lis.append(io)
        lis.append(r-1)
        lis.append(r)
        r-=2
        io+=1
    print(*lis)