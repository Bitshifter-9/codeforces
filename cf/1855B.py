t=int(input())
for i in range(t):
    n=int(input())
    cou=0
    for j in range(1,n+1):
        if n%j==0:
            cou+=1
        else:
            break
    print(cou)