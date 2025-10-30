n=int(input())
s=input()
cou=0
for i in range(n-1):
    if s[i]==s[i+1]:
        cou+=1
print(cou)
