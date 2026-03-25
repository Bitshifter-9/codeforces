import math
t=int(input())
lis=[]
pre=1
for i in range(1,t):
    if math.gcd(i,t)==1:
        lis.append(i)
        pre=pre*i%t
        # print(pre,i)
if pre!=1:
    lis.remove(pre)
print(len(lis))
print(*lis)

