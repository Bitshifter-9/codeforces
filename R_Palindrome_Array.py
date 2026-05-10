n=int(input())
lis=list(map(int,input().split()))
if lis[::-1]==lis:
    print("YES")
else:
    print("NO")