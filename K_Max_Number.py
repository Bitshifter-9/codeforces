n=int(input())
lis=list(map(int,input().split()))
ans=[float("-inf")]
def x(i):
    if i==n:
        return
    ans[0]=max(ans[0],lis[i])
    x(i+1)
x(0)
print(ans[0])