t=int(input())
for j in range(t):
    n=int(input())
    s=input()
    x=[]
    cou=0
    for i in s:
        if i not in x:
            cou+=2
            x.append(i)
        else:
            cou+=1
    print(cou)