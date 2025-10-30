n=int(input())
cou=1
su=[-1]
for i in range(n):
    s=input()
    a=s[0]
    b=s[1]
    if a==su[-1]:
        cou+=1

    su.append(b)
print(cou)
