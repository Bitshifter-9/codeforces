t=int(input())
for _ in range(t):
    n,m,i,j=map(int,input().split())
    x=set()
    x.add((1,m))
    x.add((1,1))
    x.add((n,m))
    x.add((n,1))
    ma=0
    ml=0
    mm=0
    for l,m in x:
        dis=(((i-l)**2)+((j-m)**2))**(0.5)
        if dis>=ma:
            ma=dis
            ml=l
            mm=m
    mma=0
    mml=0
    mmm=0
    for l,m in x:
        dis=(((ml-l)**2)+((mm-m)**2))**(0.5)
        if dis>=mma:
            mma=dis
            mml=l
            mmm=m
    print(ml,mm,mml,mmm)

