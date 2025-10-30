t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    x=sorted(lis)
    m=x[:n//2]
    q=x[n//2:]
    m.sort()
    q.sort()
    w=m+q
    dic={}
    ans=[]
    for j in range(n):
        dic[w[j]]=w[n-j-1]
    for k in range(n):
        ans.append(dic[lis[k]])
    print(*ans)



# firt max-first min
#secon max ki second mi
# continue like that