t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    x=input()
    y=input()
    cou=0
    while cou<10 and y not in x:
        x=x+x
        cou+=1
        if y in x:
            break
        # if cou ==5:
        #     break
    if y not in x:
        print(-1)
    else:
        print(cou)