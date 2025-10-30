t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    lis=list(map(int,input().split()))
    zero=[]
    one=[]
    for j in range(n):
        if lis[j]==0:
            zero.append(j)
        else:
            one.append(j)
    print(zero,one)

    for k in range(q):
        a,b=map(int,input().split())
        xe=[]
        on=[]
        for m in zero:
            if m<b and m>=a-1:
                xe.append(m)
        for w in one:
            if w<b and w>=a-1:
                on.append(w)
        if len(xe)%3==0 and len(on)%3==0 :
            cou=0
            st=0
            rt=0
            while st+2<len(xe):
                cou+=min(xe[st+1]-xe[st],xe[st+2]-xe[st+1])
                st+=3
 
                print(cou)
            while rt+2<len(on):
                cou+=min(on[rt+1]-on[rt],on[rt+2]-on[rt+1])
                rt+=3
            print(cou)
            

        else:
            print(-1)
        # print(xe,on)


