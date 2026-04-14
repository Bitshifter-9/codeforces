t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    a_1=[]
    b_1=[]
    c_1=[]
    for j in range(n):
        a_1.append([a[j],j])
        b_1.append([b[j],j])
        c_1.append([c[j],j])
    a_1.sort(reverse=True)
    b_1.sort(reverse=True)
    c_1.sort(reverse=True)
    a_3=a_1[:3]
    b_3=b_1[:3]
    c_3=c_1[:3]
    ans=0
    for p in range(3):
        for q in range(3):
            for r in range(3):
                if a_3[p][1]==b_3[q][1] or a_3[p][1]==c_3[r][1] or c_3[r][1]==b_3[q][1]:
                    continue
                ans=max(ans,a_3[p][0]+b_3[q][0]+c_3[r][0])
    print(ans)
        
    
