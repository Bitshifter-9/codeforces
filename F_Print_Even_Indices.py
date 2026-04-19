t=int(input())
lis=list(map(int,input().split()))
ans=[]
def x(n):
    if n<0:
        return
    ans.append(lis[n])
    x(n-2)
if t%2==0:
    x(t-2)
else:
    x(t-1)
print(*ans)