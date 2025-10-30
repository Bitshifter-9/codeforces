t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    cou_eve=0
    cou_odd=0
    for j in lis:
        if j%2==0:
            cou_eve+=1
        else:
            cou_odd+=1
    if cou_eve==0 or cou_odd==0:
        lis.sort()
        m=[]
        w=[]
        q=lis[-1]
    
        if lis.count(q)==n:
            print(-1)
        else:
            for k in lis:
                if k!=q:
                    m.append(k)
                else:
                    w.append(k)
            print(len(m),len(w))
            print(*m)
            print(*w)
    else:
        m=[]
        w=[]
        for o in lis:
            if o%2==0:
                m.append(o)
            else:
                w.append(o)
        print(len(w),len(m))
        print(*w)
        print(*m)

