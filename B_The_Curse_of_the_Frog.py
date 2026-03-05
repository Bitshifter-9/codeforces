t = int(input())
for i in range(t):
    n,x=map(int,input().split())
    lis=[]   
    for j in range(n):
        a,b,c = map(int,input().split())
        lis.append([a,b,c])    
    mi=0
    mx=0    
    for k in lis:
        st=k[0]*(k[1]-1)
        to=k[0]*k[1]-k[2]
        mi+=st
        mx=max(mx,to)    
    if mi>= x:
        print(0)
    elif mx<=0:
        print(-1)
    else:
        re=x-mi
        z=(re+mx-1)//mx
        print(z)