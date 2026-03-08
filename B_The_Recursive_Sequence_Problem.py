n,op,r=map(int,input().split())
dic={}

def ge(x):
    if x <= 1:
        return 1
    return 2 * ge(x//2) + 1
def fun(x,l,k):
    if x<=1:
        return x
    if k==l//2+1:
        return x%2
    if k<l//2+1:
        return fun(x//2,l//2,k)
    if k>l//2+1:
        return fun(x//2,l//2,k-(l//2+1))
cou=0
l=ge(n)
for m in range(op,r+1):
    z=fun(n,l,m)
    cou+=z
print(cou)

    

