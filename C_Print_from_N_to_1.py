m=int(input())
ans=[]
def x(n):
    if n==0:
        return 
    ans.append(n)
    x(n-1)
x(m)
print(*ans)