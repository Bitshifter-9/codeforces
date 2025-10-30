t=int(input())
for i in range(t):
    n=int(input())
    cou=0
    for i in range(1,n+1):
        if n%i==0:
            cou+=1
        else:
            break
    print(cou)