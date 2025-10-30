n,h=map(int,input().split())
lis=list(map(int,input().split()))
ans=n
for i in range(n):
    if lis[i]>h:
        ans+=1
print(ans)
