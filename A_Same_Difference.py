t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    cou=0
    for j in range(n-2,-1,-1):
        if s[j]!=s[-1]:
            cou+=1
    print(cou)
        