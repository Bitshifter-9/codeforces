t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    zero=lis.count(0)
    one=lis.count(1)
    if one!=0:
        print((2**(zero))*one)
    else:
        print(0)