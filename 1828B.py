import math
t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    x=[]
    for j in range(n):
        x.append(0)
    # print(x)
    for k in range(n):
        x[k]=(abs(k-lis[k]+1))
    x.sort()
    cou=0
    ma=0
    num=0
    ans=[]
    for k in x:
        if k!=0:
            ans.append(k)
    # print(ans)
    wei=ans[0]
    for l in ans:
        wei=math.gcd(wei,l)
    print(wei)
    