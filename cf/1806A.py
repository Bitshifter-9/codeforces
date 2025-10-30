t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    cou=0
    if d>b:
        cou+=(d-b)
      
        b+=cou
        a+=cou
 
    if a>c:
        cou+=(a-c)
        a=c
    if a==c and b==d:

        print(cou)
    else:
        print(-1)

