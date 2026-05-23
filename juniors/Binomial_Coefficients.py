import math

t=int(input())
dic={0:1}
  
rec=1
for j in range(1,10**6+1):
    rec=(rec*j)%(10**9+7)
    dic[j]=rec
for i in range(t):
    a,b=map(int,input().split())
   
    ag=dic[a]%(10**9+7)
    bg=dic[b]%(10**9+7)
    cg=dic[a-b]%(10**9+7)
    ans1=pow(cg*bg,10**9+7-2,(10**9+7))
    ans2=(ag*ans1)%(10**9+7)
    print(ans2)


