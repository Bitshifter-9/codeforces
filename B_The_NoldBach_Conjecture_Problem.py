n,k=map(int,input().split())
x=[True]*(n+1)
ans=[]
for i in range(2,n+1):
    if x[i]:
        ans.append(i)
        j=2*i
        while j<=n:
            x[j]=False
            j+=i
m=len(ans)//2
se=set(ans)
cou=0
for j in range(len(ans)-1):
    m=1+ans[j]+ans[j+1]
    # print(m)
    if m in se:
        cou+=1
# print(cou)
if cou>=k:
    print("YES")
else:
    print("NO")