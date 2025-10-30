n=int(input())
for i in range(n):
    s=input()
    m=len(s)
    if m%2==0:
        if s[:m//2]==s[m//2:]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
