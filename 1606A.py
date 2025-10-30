t=int(input())
for i in range(t):
    s=input()
    ab=0
    ba=0
    if s[0]==s[-1]:
        print(s)
    elif s[0]=="a":
        print("b"+s[1:])
    else:
        print("a"+s[1:])
