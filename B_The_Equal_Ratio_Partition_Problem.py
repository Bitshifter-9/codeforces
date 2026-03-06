import math
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    d=0
    k=0
    m={}
    ans=[]
    for j in range(n):
        if s[j]=="D":
            d+=1
        else:
            k+=1
        gcd=math.gcd(d,k)
        z=(d//gcd,k//gcd)
        if z in m:
            m[z]+=1
        else:
            m[z]=1
        ans.append(m[z])
    # print(len(ans))
    print(*ans)
        

