t=int(input())
for i in range(t):
    n,p=map(int,input().split())
    lis=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    cou=1
    num=0
    cos=p
    x=[]
    for j in range(n):
        x.append([arr[j],lis[j]])
    x.sort()


    for j in range(n):
        if cou>=n:
            break
        if x[j][0]<p :
            w=min(x[j][1],n-cou)
            cos+=x[j][0]*w
            cou+=w
        else:
            break
     
   
    # cos+=(num*p)
    # print(cou)
    cos+=(n-cou)*p
    print(cos)


            

            
            