s=input()
dic={}
import math
z=0
for j in s:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
    z=max(z,dic[j])
fac={}
tu=1
for m in range(1,len(s)+1):
    tu=(tu*m)%(10**9+7)
    fac[m]=tu
qq=1
for jp in dic:
    qq=(qq*fac[dic[jp]])%(10**9+7)
rt=pow(qq,10**9+7-2,10**9+7)

print((rt*tu)%(10**9+7))





