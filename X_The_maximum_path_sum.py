n,m=map(int,input().split())
arr=[]
for j in range(n):
    lis=list(map(int,input().split()))
    arr.append(lis)
an=[]
def x(i,j,ans):
    if i>=n or j>=m:
        return
    if i==n-1 and j==m-1:
        q=sum(ans)
        q+=arr[i][j]
        an.append(q)
        return
    
    x(i+1,j,ans+[arr[i][j]])
    
    x(i,j+1,ans+[arr[i][j]])
x(0,0,[])
print(max(an))
# print(arr)



