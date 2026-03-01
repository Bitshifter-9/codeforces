t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    dic={}
    op=len(set(lis))

    if op==1:
        if n%2==0:
            print(0)
        else:
            print(2)
    else:
        for j in range(2*n):
            if lis[j] in dic:
                dic[lis[j]] = dic[lis[j]]+1
            else:
                dic[lis[j]]=1
        a=[]
        b=[]
        q=len(set(lis))
        ind=0
        wep=0
        w=0
        e=0
        for m in dic:
            if dic[m]%2==0:
                w+=1
                if (dic[m]//2)%2!=0 and dic[m]//2!=0:
                    ind+=1
                else:
                    wep+=1
            else:
                e+=1
        ans=e+2*w
        if e==0:
            if w%2!=n%2:
                ans-=2
        print(ans)







            

                   
                            
