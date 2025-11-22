t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print(0)
    else:
        cou=0
        w=n
        if w%2==0:
            while w%2==0:
                w=w//2
            # print(w)
        if w==1:
            print(-1)
        else:

            while n%6!=0:
                n*=2
                cou+=1
                
                # print(n)
            while n%6==0:
                n//=6
                cou+=1
            print(n,cou)
            # if n==1:
            #     print(cou)
            # else:

            #     print(-1)
            