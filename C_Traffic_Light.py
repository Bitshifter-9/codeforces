t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    s=input()
    w=[]
    r=[]
    y=[]
    g=[]
    x=0
    q=0
    z=0
    for k in range(int(a)):
        if s[k]=="r":
            x+=1
            r.append(k)
        elif s[k]=="y":
            q+=1
            y.append(k)
        elif s[k]=="g":
            z+=1
            g.append(k)
        # r.append(x)
        # y.append(q)
        w.append(s[k])
        # g.append(z)
    if b=="r":
        ma=float("-inf")
        for j in r:
            left=0
            right=len(g)-1
            re=-1
            while left<=right:
                mid=(left+right)//2
                if g[mid]>j:
                    right=mid-1
                    re=g[mid]
                    
                elif g[mid]<=j:
                    left=mid+1
            if re==-1:
                if len(g)>0:
                    re=int(a)-j+g[0]
                    ma=max(ma,re)
            else:
                ma=max(ma,re-j)
        print(ma)
    elif b=="y":
        ma=float("-inf")
        for j in y:
            left=0
            right=len(g)-1
            re=-1
            while left<=right:
                mid=(left+right)//2
                if g[mid]>j:
                    right=mid-1
                    re=g[mid]
                    
                elif g[mid]<=j:
                    left=mid+1
            if re==-1:
                if len(g)>0:
                    re=int(a)-j+g[0]
                    ma=max(ma,re)
            else:
                ma=max(ma,re-j)
        print(ma)
    else:
        print(0)

     
