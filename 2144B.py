t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    x=[]
    m={}
    for k in lis:
        if k in m:
            m[k]=m[k]+1
        else:
            m[k]=1

    for j in range(1,n+1):
        if j in m:
            continue
        else:
            x.append(j)
    
    for j in range(len(lis)):
        if lis[j]==0:
            lis[j]=x[-1]
            x.pop()
    # print(lis)
    st=-1
    end=-1
    for j in range(len(lis)):
        if lis[j]!=j+1:
            if st==-1:
                st=j+1
            else:
                end=j+1
    if st==-1 and end==-1:
        print(0)
    else:
        print(end-st+1)
