# t=int(input())
# arr=[]
# if t==1:
#     print(f"{0:.15f}")
# else:
#     for j in range(t):
#         arr.append([])
#     for i in range(t-1):
#         a,b=map(int,input().split())
#         arr[a-1].append(b-1)


#     def dfs(k):
#         vis[k] = 1
#         q.append(k)

  
#         if len(arr[k]) == 0:
#             ans.append(len(q[:])-1)
#         else:
#             for nxt in arr[k]:
#                 if not vis[nxt]:
#                     dfs(nxt)

#         q.pop()  
            

        
        
                
#     ans=[]
#     ar=[]
#     for i in arr[0]:
#         vis=[0]*t
#         q=[0]
#         dfs(i)
#         ar.append(q[:])
#         # ans.append(len(q[:])-1)
#     # print(arr)

#     # print(ar)
#     # print(ans)
#     print(f"{sum(ans)/len(ans):.15f}")


import sys
sys.setrecursionlimit(200000)

t = int(input())
arr = [[] for _ in range(t)]

for _ in range(t - 1):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)  

def dfs(node, parent):
    total = 0.0
    count = 0
    for nxt in arr[node]:
        if nxt != parent:
            total += dfs(nxt, node) + 1 
            count += 1
    if count == 0:
        return 0.0  
    return total / count  

ans = dfs(0, -1)
print(f"{ans:.15f}")



