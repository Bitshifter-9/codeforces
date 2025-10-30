ans=[]
def x(n):
    if n<=0:
        return
    ans.append(1)
    x(n//2)
x(5)
print(sum(ans))
    