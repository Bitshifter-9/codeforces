n,k=map(int,input().split())
lis=list(map(int,input().split()))
cou=0
for i in range(n):
    if lis[i]>=lis[k-1] and lis[i]>0:
        cou+=1
print(cou)