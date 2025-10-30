t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    s=set(lis)
    q=list(s)
    q.sort()
    ans=False
    for j in range(len(q)):
        if q[j]!=j:
            print(j)
            ans=True
            break
    if ans==False:
        print(len(q))
