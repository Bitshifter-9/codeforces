import math
t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    for j in range(1,61):
        se=set()
        cou=0
        for op in lis:
            m=op%(2**j)
            if m not in se:
                se.add(m)
                cou+=1
        if cou==2:
            print(2**j)
            break

