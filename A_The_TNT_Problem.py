t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    # lis.sort()
    # print((n-2)/n)
    if n==1:
        print(0)
    else:
        ma=float("-inf")
        arr=[]
        for m in range(1,n):
            if n%m==0:
                arr.append(m)
        mb=float("-inf")
        for k in arr:
            op=float("-inf")
            oz=float("inf")
        
            for j in range(0,n,k):
            
                we=sum(lis[j:j+k])
                op=max(op,we)
                oz=min(oz,we)
            mb=max(mb,op-oz)
        if mb==float("-inf"):
            mb=0
        print(mb)





