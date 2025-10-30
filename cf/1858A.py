t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a>b:
        print("First")
    elif a==b:
        if c%2!=0:
            print("First")
        else:
            print("Second")
    else:
        print("Second")