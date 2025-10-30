t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    s=set(lis)
    print(len(s)+len(s)-1)