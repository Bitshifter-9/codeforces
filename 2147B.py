t=int(input())
for i in range(t):
    n=int(input())
    x=[]
    for j in range(1,n+1):
        x.append(n-j+1)

    x.append(n)
    for k in range(1,n):
        x.append(k)
    print(*x)