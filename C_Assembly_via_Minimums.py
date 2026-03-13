t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    # dic={}
    # for j in lis:
    #     if j in dic:
    #         dic[j]+=1
    #     else:
    #         dic[j]=1
    # arr=[]
    # for m in dic:
    #     arr.append([dic[m],m])
    # arr.sort(reverse=True)
    # print(arr)
    lis.sort()
    x=n-1
    i=0
    arr=[]
    while x>0:
        arr.append(lis[i])
        i+=x
        x-=1
    arr.append(max(lis))
    print(*arr)
