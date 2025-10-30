n=int(input())
for i in range(n):
    lis=list(map(str,input().split()))
    s=""
    for j in lis:
        s=s+j[0]
    print(s)