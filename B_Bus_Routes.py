t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    vis=[0]*(a+1)
    for i in range(b):
        c,d=map(int,input().split())
        vis[c-1]=+1
        vis[d]=-1
    # print(vis)
    co=0
    ans=0
    q=[]
    # for j in range(len(vis)):
    #     co+=vis[j]
    #     if co<=0 and j+1<len(vis)-1 and vis[j+1]!=0:
    #         ans+=1
    for j in vis:
        co+=j
        q.append(co)
    print(vis,q)
       
    # print(ans)
    # x=[]
    # for i in range(a):
    #     x.append([])
    # for j in range(b):
    #     c,d=map(int,input().split())
    #     x[c-1].append(d)
    #     x[d-1].append(c)
    # vis=[0]*a
    # co=[]
    # def dfs(i):
    #     vis[i]=1
    #     for j in x[i]:
    #         if vis[j-1]==0:
    #             dfs(j-1)
    

    # def q():
    #     for i in range(a):
    #         if vis[i]==0:
    #             dfs(i)
    #             co.append(1)
    # q()
    # print(sum(co))
                    
                
            
    