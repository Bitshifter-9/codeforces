n,td=map(int,input().split())
lis=list(map(int,input().split()))
z=max(lis)*max(lis)
x=[True]*(z+1)
ans=list(range(z+1))
for i in range(2,int(z**0.5)+1):
    if ans[i]==i:
        ans.append(i)
        for j in range(i*i,z+1,i):
            if ans[j]==j:
                ans[j]=i
# print(ans)
f=set()
def fact(k):
   
    po=1
    while k>1:
        if ans[k] not in f:
            po*=ans[k]
        f.add(ans[k])

        k//=ans[k]
    # return po
pre=[]
# print(fact(10))
for op in lis:
    fact(op)
fec=list(f)

for lp in fec:
    for io in fec:
        if io!=lp:
            f.add(lp*io)
print(f)
se_3=set()
se_2=set()
on_e=0
for ne in range(n):
    for me in range(ne+1,n):
        se_2.add(lis[ne]*lis[me])
    se_3.add(lis[ne])
    if lis[ne]==1:
        on_e+=1
    
print(se_2)
cou_3=0
for zp in f:
    if zp**td in se_2:
        cou_3+=1
    if zp**td in se_3:
        print("ye")
        if on_e>1 and zp==1:
            cou_3+=(on_e*(on_e-1))
        elif zp!=1:
            cou_3+=on_e
print(cou_3)

    


