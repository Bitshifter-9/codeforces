import math
s=input()
v=[]
o=[]
co_v=0
co_o=0
for i in range(len(s)-1):
    if s[i]=="v" and s[i+1]=="v":
        co_v+=1
     
    if s[i]=="o":
        
        o.append(i)
    v.append(co_v)
# print(v,o)
x=0
for j in o:
    left=v[j-1]
    right=v[-1]-left

    x+=((left)*(right))
print(x)
    
