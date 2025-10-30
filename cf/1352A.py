t=int(input())
for i in range(t):
    n=int(input())
    s=str(n)
    x=[]
    co=0
    m=[]
    for j in s:
        if co==0:
            m.append(j)
        elif j=="0":
            m.append(j)
        else:
            m.append("0"*(len(s)-co))
            x.append(m[:])
            m=[]
            m.append(j)
        co+=1
    x.append(m)
    print(len(x))
    for l in x:
        print("".join(l),end=" ")
    print()
            
