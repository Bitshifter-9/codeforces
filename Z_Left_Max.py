t=int(input())
lis=list(map(int,input().split()))
arr=[lis[0]]
for j in range(1,t):
    arr.append(max(arr[-1],lis[j]))
print(*arr)
