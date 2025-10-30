t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n*n-1==k:
        print("NO")
    else:
        cou=0
        lis=[]
        ans=True
        xxx = True
        end = (k // n)
        
        for j in range(n):
            x=[]
            for m in range(n):
                if cou<k:
                    x.append("U")
                    cou+=1
                else:
                    
                    if ans and j != n-1:
                        x.append("D")
                        ans = False
                        xxx = False
                    else:
                        if m==0:
                            x.append("R")
                        elif m == n-1 and j==n-1 and j==end:
                            x.append("L")
                        elif j==n-1 and j==end:
                            x.append("R")
                        else:
                            x.append("L")
                        
            lis.append(x)
        print("YES")
        for o in range(n):
            print("".join(lis[o]))

        

