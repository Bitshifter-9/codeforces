t=int(input())
for i in range(t):
    n=int(input())
    x=n
    su=0
    cou=len(str(n))-1

    while cou>0:
        su+=n//(10**cou)
        n=10**(cou)-1
        
        cou-=1
        

    if x>=10:


        print(su+9)
    else:
        print(x)