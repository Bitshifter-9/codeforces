t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    ma=float("inf")
    me=float("inf")
    ind1=-1
    ind2=-1
    pre_m=[]
    suf_ma=[[0,0] for k in range(n)]
    for j in range(n):
        if ma>lis[j]:
            ma=lis[j]
            ind1=j
            pre_m.append([ma,ind1])
        else:
            pre_m.append([ma,ind1])
        if me>lis[n-j-1]:
            me=lis[n-j-1]
            ind2=n-j-1
            suf_ma[n-j-1]=[me,ind2]
        else:
            suf_ma[n-j-1]=[me,ind2]
    ans=False
    arr=[]
    # print(pre_m,suf_ma)
    for k in range(1,n-1):
        if lis[k]>pre_m[k-1][0] and lis[k]>suf_ma[k+1][0]:
            print("YES")
            print(pre_m[k-1][1]+1,k+1,suf_ma[k+1][1]+1)
            
            ans=True
            break
    if ans==False:
        print("NO")

