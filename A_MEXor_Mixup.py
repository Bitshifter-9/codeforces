t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    cou=0
    if a == 1 and b == 0:
        print(2)
    for i in range(a):
        cou=cou^i
    if cou==b:
        print(a)
    elif a==1 and b==1:
        print(3)
    else:
        print(a+1)
    
