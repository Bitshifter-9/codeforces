t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    num=lis[0]
    mi=lis[0]
    for j in range(1,n):
        mi=min(lis[j],mi)
    if mi==num:
        print("YES")
    else:
        print("NO")