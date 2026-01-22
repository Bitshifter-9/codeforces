t=int(input())
import math
for j in range(t):
    n=int(input())
    lis=[]
    m=2
    for i in range(1,n+1):
        lis.append(i * (i + 1))
        # m*=2
    print(*lis)
    # for io in range(n-1):
    #     print(math.gcd(lis[io],lis[io+1]))