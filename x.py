t=int(input())
lis=list(map(int,input().split()))
dic={0}
se=set()
for i in lis:
    se=set()
    for j in dic:
        se.add(j+i)
    dic |=se
arr=list(dic)
arr.sort()
arr=arr[1:]
print(len(arr))
print(*arr)
