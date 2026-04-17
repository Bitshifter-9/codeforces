# n,m=map(int,input().split())
# x=[True]*(n+1)
# ans=[]
# for i in range(2,n+1):
#     if x[i]:
#         ans.append(i)
#         j=2*i
#         while j<=n:
#             x[j]=False
#             j+=i
# vis=[0]*(n+1)
# se=set()
# dic={}
# for zhs in ans:
#     dic[zhs]=0
# for k in range(m):
#     s=input()
#     z=int(s[2:])
#     if s[0]=="-":
#         if vis[z]==0:
#             print("Already off")
#         else:
#             vis[z]=0
#             for jp in dic:
#                 if z%jp==0:
#                     dic[jp]=0
#             se.remove(int(s[2]))

#             print("Success")

#     else:
#         num=int(s[2:])
#         if vis[num]==1:
#             print("Already on")
#         else:
#             div=[]
#             an=True
#             for op in ans:
#                 if num%op==0:
#                     if dic[op]!=0:
#                         an=False
#                         break
#                     div.append(op)
#             if an:
#                 for k in div:
#                     dic[k]=1
#                 print("Success")
#                 se.add(num)
#                 vis[num]=1
#             else:
#                 con=-1
#                 z=int(s[2:])
#                 for op in se:
#                     for mp in ans:
#                         if op%mp==0 and z%mp==0:
#                             con=op
#                             break
#                 print(f'Conflict with {con}')

n, m = map(int, input().split())
spf = list(range(n + 1))
for i in range(2, int(n ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, n + 1, i):
            if spf[j] == j:
                spf[j] = i
print(spf)

def fact(x):
    f = set()
    while x > 1:
        f.add(spf[x])
        x //= spf[x]
    return f

# vis = [0] * (n + 1)
# dic = [0] * (n + 1)

# for _ in range(m):
#     s, z = input().split()
#     z = int(z)

#     if s == '+':
#         if vis[z]:
#             print("Already on")
#         else:
#             ok = True
#             f = fact(z)
#             for p in f:
#                 if dic[p]:
#                     print(f"Conflict with {dic[p]}")
#                     ok = False
#                     break
#             if ok:
#                 for p in f:
#                     dic[p] = z
#                 vis[z] = 1
#                 print("Success")
#     else:
#         if not vis[z]:
#             print("Already off")
#         else:
#             f = fact(z)
#             for p in f:
#                 dic[p] = 0
#             vis[z] = 0
#             print("Success")


                        



