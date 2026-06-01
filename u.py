import sys
sys.setrecursionlimit(10**7)

a,b=map(int,input().split())
lis=list(map(int,input().split()))
lis.sort()
# dic={}
# def x(su,i):
#     if su==b:
#         # print(su)
#         return 0
#     if su>b or i>=a:
#         return float("inf")
#     if (su,i) in dic:
#         return dic[(su,i)]
#     ans=float("inf")
#     if su+lis[i]<=b:
#         ans=1+x(su+lis[i],i)
#     ans_2=x(su,i+1)
#     dic[(su,i)]=min(ans,ans_2)
#     return dic[(su,i)]
# z=x(0,0)
# if z==float("inf"):
#     print(-1)
# else:
#     print(z)

a = len(lis)

dp = [float("inf")] * (b + 1)
dp[0] = 0   

for i in range(a):
    for su in range(lis[i], b + 1):
        dp[su] = min(dp[su], 1 + dp[su - lis[i]])

if dp[b] == float("inf"):
    print(-1)
else:
    print(dp[b])

