t=int(input())
for i in range(t):
    n=int(input())
    s=str(n)
    mi=float("inf")
    for j in s:
        mi=min(mi,int(j))
    print(mi)