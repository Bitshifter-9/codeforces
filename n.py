n=int(input())
ans=[]
x=[]

for i in range(n):
    m=[]
    for j in range(n):
        m.append(".")
    x.append(m)
# print(x[0][0][1])


vis=[]
dia=[]
antidia=[]

def bac(r):
    if r==n:
    
        solution = [row[:] for row in x]   # deep copy of the whole board
        ans.append(solution)
        return
    # print(r)

    for i in range(n):
        su_m=r+i
        dif=r-i
        if not((su_m  in antidia) or (dif in dia) or (i  in vis)):           
           
            antidia.append(su_m)
            dia.append(dif)
            vis.append(i)
            x[r][i]='Q'
            # print(vis)
            bac(r+1)
            antidia.pop()
            dia.pop()
            vis.pop()
            x[r][i]="."


            # print(vis)      
bac(0)



print(ans[0])        
           

