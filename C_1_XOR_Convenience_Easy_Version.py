t= int(input())
for i in range(t):
    n = int(input())
    if n%2==0:
        print(-1)
    else:
        lis=[]
        for j in range(1,n+1):
            lis.append(j)
        for k in range(1,n-1,2):
            lis[k+1],lis[k]=lis[k],lis[k+1]
            # print(lis)
        lis[0],lis[-1]=lis[-1],lis[0]
        print(*lis)
# print(6^1)

