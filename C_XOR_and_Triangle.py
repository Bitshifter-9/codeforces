t=int(input())
for i in range(t):
    x=int(input())
    a=1
    while x%(2*a)==0:
        a*=2
    b=1
    t=x
    while t%2==1:
        t//=2
        b*=2
    y=a+b
    if y<x:
        print(y)
    else:
        print(-1)


