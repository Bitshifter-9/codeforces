t=int(input())
for i in range(t):
    a,b,n=map(int,input().split())
    if a/n==b:
        print(1)
    else:
        if a/n<b:
            if a<=b:
                print(1)
            else:

               print(2)
        else:
            print(1)

    # print(a/n<b)
    