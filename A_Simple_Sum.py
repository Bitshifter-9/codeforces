t=int(input())
x,n,m=map(int,input().split())
def fun(x,m):
    if m==0:
        return 1
    we=(1+x)*fun(x**2,m//2)
    return we
oi=fun(x,m)
print(oi)