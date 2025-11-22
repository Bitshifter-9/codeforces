import heapq
t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    arr=[]
    arr1=[]
    arr2=[]
    for j in range(len(lis)):
        heapq.heappush(arr,(-lis[j],j))
    print(arr)
