t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    x=[]
    for i in range(k):
        a,b=map(int,input().split())
        x.append((a,b))
    x.sort()
    if k==0:
        print(n-1)
    # print(x)
    elif len(x)>0:
        q=[[x[0][0],x[0][1]]]
        index=0
        for i in range(1,len(x)):
            if x[i][0]<=q[index][1]:
                q[index][1]=max(q[index][1],x[i][1])
               
            else:
                q.append([x[i][0],x[i][1]])
                index+=1
        poi=0
        for j in range(1,len(q)):
            poi+=(q[j][0]-q[j-1][1])
        poi+=(q[0][0]-1)
        poi+=n-q[-1][1]

        print(poi)
    # else:
    #     print(0)

  

