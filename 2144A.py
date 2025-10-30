t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    if sum(lis)%3!=0:
        print(0,0)
    else:
        print(n-2,n-1)