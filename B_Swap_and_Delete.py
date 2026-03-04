
t = int(input())
idx = 1

for _ in range(t):
    s = input()
    
    c0 = s.count('0')
    c1 = len(s) - c0

    le=0
    for i in range(len(s)):
        if s[i]=="0" and c1>0:
            c1-=1
            le+=1
        elif s[i]=="1" and c0>0:
            c0-=1
            le+=1
        else:
            break
    print(len(s)-le)
