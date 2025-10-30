n,m=map(int,input().split())
lis=[]
for i in range(n):
    lis.append([])

for j in range(m):
    a,b=map(int,input().split())
    lis[a-1].append(b)
    lis[b-1].append(a)
vis=[0]*n

def dfs(i):
    if vis[i-1]==0:
        vis[i-1]=1
        for j in lis[i-1]:
            dfs(j)


cou=[]
ans=[]
def x():
    for i in range(1,n+1):
        if vis[i-1]==0:
            cou.append(1)
            ans.append([i-1,i])
            dfs(i)
x()

           
print(sum(cou)-1)
for i in range(1,len(ans)):
    print(ans[i][0],ans[i][1])
# print(ans)
