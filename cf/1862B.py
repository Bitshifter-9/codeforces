t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    x=[lis[0]]
    for j in range(1,n):
        if lis[j]<lis[j-1]:
            x.append(lis[j])
        x.append(lis[j])
    print(len(x))
    print(*x)