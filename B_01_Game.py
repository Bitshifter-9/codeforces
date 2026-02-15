t=int(input())
for i in range(t):
    s=input()
    a=s.count("0")
    b=s.count("1")
    x=min(a,b)
    if x%2!=0:
        print("DA")
    else:
        print("NET")