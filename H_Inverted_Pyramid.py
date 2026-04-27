n=int(input())
ans=[]
def x(m,i):
    if m==0:
        return
    op=" "*i+"*"*(2*m-1)
    ans.append(op)
    x(m-1,i+1)
x(n,0)
# ans.reverse()

for _ in ans:
    print(_)
