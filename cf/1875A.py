t=int(input())
for i in range(t):
    a,b,n=map(int,input().split())
    lis=list(map(int,input().split()))
    cou=b
    for j in lis:
        if j<a:
            cou+=(j-1)
        else:
            cou+=(a-1)
    print(cou)