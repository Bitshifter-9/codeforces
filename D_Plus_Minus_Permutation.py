import math
t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    su=0
    m=x
    ind=1
    m=n//x
    hp=n//(math.lcm(x,y))
    op=n*(n+1)//2-((n-m+hp)*(n-m+1+hp)//2)
    qp=n//y
    zo=(qp-hp)*(qp+1-hp)//2
    print(op-zo)
    

