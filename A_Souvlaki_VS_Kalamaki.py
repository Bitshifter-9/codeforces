t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    lis.sort()
    for j in range(1,n-1,2):
        if lis[j]!=lis[j+1]:
            print("NO")
            break
    else:
        print("YES")
        