ma=10**6
x=list(range(ma+1))
pri=[]
for i in range(2,int(ma+1)):
    if x[i]==i:
        pri.append(i)
        for j in range(i*i,ma+1,i):
            if x[j]==j:
                x[j]=i
# print(len(pri))
t=int(input())
for k in range(t):
    n=int(input())
    lis=[]
    for io in range(n):
        lis.append(pri[io]*pri[io+1])
    print(*lis)

# import math
# m=200000
# primes=[True for _ in range(m+1)]
# primes[0]=primes[1]=False
# for i in range(2,int(m**0.5)+1):
#     if primes[i]:
#         for j in range(i*i,m+1,i):
#             primes[j]=False
# prm=[i for i in range(len(primes)) if primes[i]]
# for _ in range(int(input())):
#     n=int(input())
#     a=[]
#     for i in range(n):
#         a.append(prm[i]*prm[i+1])
#     print(*a)