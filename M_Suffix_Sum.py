n,m=map(int,input().split())
lis=list(map(int,input().split()))
# ans=[0]
# def x(i):
#     if i==n-m-1:
#         return
#     ans[0]+=lis[i]
#     x(i-1)
# x(n-1)
# print(ans[0])
a=sum(lis[:n-m])
print(sum(lis)-a)