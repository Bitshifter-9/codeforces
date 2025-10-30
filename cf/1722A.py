t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    cou=0
    if len(s)==5:
        if "T" in s and "i" in s and "m" in s and "u" in s and "r" in s:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")