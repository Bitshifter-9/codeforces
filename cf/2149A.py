t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    ans=0
    mi_on=lis.count(-1)
    zero=lis.count(0)
    one=lis.count(1)
    ans+=zero
    if mi_on%2==0:
        print(ans)
    else:
        print(ans+2)
