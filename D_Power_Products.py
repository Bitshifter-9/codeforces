n,k=map(int,input().split())
lis=list(map(int,input().split()))
z=max(lis)
spf=list(range(z+1))
for i in range(2,z+1):
    if spf[i]==i:
        for j in range(2*i,z+1,i):
            if spf[j]==j:
                spf[j]=i

print(spf)
def fact(x):
    ;
arr=[]
for k in lis:
