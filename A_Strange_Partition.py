t=int(input())
import math
for _ in range(t):
    a,b=map(int,input().split())
    lis=list(map(int,input().split()))
    co=0
    
    for i in range(a):
        co+=math.ceil(lis[i]/b)
    ku=math.ceil(sum(lis)/b)
    print(ku,co)