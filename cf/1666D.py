t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    x=[]
    for j in a:
        if j in b:
            x.append(j)
  
    ans="YES"
    if len(x)>0 and len(b)>0 and x[-1]!=b[-1]:
        ans="NO"
    else:
        o=len(b)-1
        cou=0
        po_p=[]
        for k in range(len(x)-1,-1,-1):            
            if x[k]==b[o] and o>=0 and x[k] not in po_p:         
                cou+=1
                o-=1
            else:
                po_p.append(x[k])
        if cou!=len(b):
            ans="NO"       
    print(ans)
