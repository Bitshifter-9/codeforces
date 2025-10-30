t=int(input())
for o in range(t):
    n=int(input())
    
    i=1
    j=2
    print(i,j)
    p=int(input())
    no=[]
    while p!=0:
        no.append(i)
        i+=1
        j+=1
        print(i,j)
        x=int(input())
        p=x
    print(no)
