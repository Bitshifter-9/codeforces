n=int(input())
x=[True]*(n+2)
ans=[]
vis=[False]*(n+2)
z=[1]*(n+2)
we=False
for i in range(2,n+2):
    if x[i]:
        ans.append(i)
        j=2*i
        while j<=n+1:
            x[j]=False
            if vis[j]==False:
                z[j]+=1
                we=True
                vis[j]=True
            j+=i
dic={}
cou=1
if we:
    cou+=1
print(cou)
print(*z[2:])

# for m in ans:


# for k in range(2,n+2):
    

