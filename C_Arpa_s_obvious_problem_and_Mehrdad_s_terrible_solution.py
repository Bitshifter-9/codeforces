t,n=map(int,input().split())
lis=list(map(int,input().split()))
x={}
cou=0
index=0
for i in lis:
    if i^n in x and x[i^n]>0:
        cou+=x[i^n]


    if i not in x:
        x[i]=1
    else:
        x[i]=x[i]+1
print(cou)
# print(x)