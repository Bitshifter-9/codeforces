t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    lis=list(map(int,input().split()))
    ans="NO"
    cou=0
    for j in range(n):
        if lis[j]==k:
            ans="YES"
            break
    print(ans)