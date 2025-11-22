t=int(input())
for i in range(t):
    n=int(input())
    lisw=list(map(int,input().split()))
    cos=0
    for j in range(n):
        cos+=max(lisw[j],lisw[(j+1)%n])
    print(cos-max(lisw))
