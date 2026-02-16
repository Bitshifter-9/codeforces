t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    zero=lis.count(0)
    print(min(n-zero,sum(lis)-n+1))

    


   