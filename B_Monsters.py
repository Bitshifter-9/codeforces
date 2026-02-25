import heapq
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    lis=list(map(int,input().split()))
    x=[]
    ind=0
    for j in lis:
        m=j%k
        if m==0:
            x.append([k,ind])

        else:
            x.append([m,ind])
        ind+=1
    x.sort(key=lambda x: (-x[0], x[1]))
    # print(x)
    for o in range(n):
        print(x[o][1]+1,end=" ")
    print(" ")
   
    
    