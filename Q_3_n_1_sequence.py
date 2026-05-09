n=int(input())
x=[n]
for j in range(3*n+1):
    if x[-1]==1:
        break
    if x[-1]%2==0:
        x.append(x[-1]//2)
    else:
        x.append(3*(x[-1])+1)
   
print(len(x))