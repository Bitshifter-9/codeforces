n=int(input())
spf=list(range(n+1))
cou=0
dic={}
for i in range(2,n+1):
    if spf[i]==i:
        cou+=1
        dic[spf[i]]=cou
        for k in range(2*i,n+1,i):
            if spf[k]==k:
                spf[k]=i
x=spf[2:]
cou=1
se=set()
for m in range(len(x)):
    x[m]=dic[x[m]]
print(*x)
