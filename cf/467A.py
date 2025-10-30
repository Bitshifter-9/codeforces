t=int(input())
cou=0
for i in range(t):
    a,b=map(int,input().split())
    if b-a>=2:
        cou+=1
print(cou)