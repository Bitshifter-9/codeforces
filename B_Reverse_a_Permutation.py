t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    suf=[]
    ma=float("-inf")
    ans=-1
    
    for j in range(n):
        if lis[j]!=n-j:
            ans=j

            break
    if ans==-1:
        print(*lis)
    else:
        che=-1
        for k in range(n):
            if lis[k]==n-ans:
                che=k
                break
        
        m=lis[ans:che+1]
        m.reverse()
        z=lis[:ans]+m+lis[che+1:]

        print(*z)

        

    