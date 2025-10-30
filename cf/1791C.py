t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    cou=0
    while len(s)>0 and s[0]!=s[-1]:
        s=s[1:-1]
    print(len(s))