t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))

    pre=[]

    ans=1

    for j in range(n):
        ans*=lis[j]

        pre.append(ans)

      
    ans=-1

    for  j in range(n):
        m=pre[-1]//pre[j]
        if m==pre[j]:
            ans=j+1
            break
    print(ans)
