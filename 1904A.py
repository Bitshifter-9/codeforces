t=int(input())
for i in range(t):
    h1,h2=map(int,input().split())
    k1,k2=map(int,input().split())
    q1,q2=map(int,input().split())
    cou=0
    ans=[[k1-h1,k2-h2],[k1-h1,k2+h2],[k1+h1,k2-h2],[k1+h1,k2+h2],[k1-h2,k2-h1],[k1-h2,k2+h1],[k1+h2,k2-h1],[k1+h2,k2+h1]]
    arr=[]
    for j in ans:
        if [j[0],j[1]] not in arr:
            arr.append(j)
    
    # print(arr)
    for k in arr:
        x=k[0]
        y=k[1]
        if (x-h1,y-h2)==(q1,q2) or (x-h1,y+h2)==(q1,q2)or(x+h1,y-h2)==(q1,q2)or(x+h1,y+h2)==(q1,q2)or(x-h2,y-h1)==(q1,q2)or(x-h2,y+h1)==(q1,q2)or(x+h2,y-h1)==(q1,q2)or(x+h2,y+h1)==(q1,q2):
            cou+=1
    print(cou)
        