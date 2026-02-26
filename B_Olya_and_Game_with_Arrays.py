import heapq
t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for j in range(n):
        t=int(input())
        lis=list(map(int,input().split()))
        lis.sort()
        a.append(lis)
    ind=0
    ans=0
    w=0
    for p in range(n):
        w+=a[p][1]
    ans=0
    an=float("inf")
    for uy in range(n):
        an=min(an,a[uy][0])

    for iu in range(n):
        z= w - a[iu][1]
        z=z+an
        ans=max(ans,z)
        

    print(ans)





        