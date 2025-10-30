k,n,w=map(int,input().split())
x=k*(w*(w+1)//2)
if x<=n:
    print(0)
else:
    print(x-n)
