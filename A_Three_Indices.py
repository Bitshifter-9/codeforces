t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    # ml=[]
    # mn=0
    # for j in range(n):
    #     mn=max(mn,lis[j])
    #     ml.append(mn)
    # maxr=[]
    # mr=0
    # for k in range(n-1,-1,-1):
    #     mr=max(mr,lis[k])
    #     maxr.append(mr)
    # print(ml,maxr)

    if lis[0]==max(lis):
        print('No')
    q1=[(lis[0],0)]
    q2=[]

    for i in range(1,n):
        if lis[i]>q1[-1]:
            q2.append[(lis[i],i)]
        
        if q2[-1]
    