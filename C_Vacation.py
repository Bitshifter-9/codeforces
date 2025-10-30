t=int(input())
arr=[]
for i in range(t):
    lis=list(map(int,input().split()))
    arr.append(lis)
m={}
# for j in arr[0]:
#     print(j)
po=[]
def x(i,no):
    if i==len(arr):
        return 0
    key = (i, no)  # memoization key
    if key in m:
        po.append(1)
        return m[key]
    ma=0
    cou=0
    for j in range(3):
        if no!=-1:
            if no==j:
                continue

        qw=arr[i][j]+x(i+1,j)
        if qw>ma:
            ma=qw
            ind=j
        ma=max(ma,qw)
    # rt=i*10+j
    m[key] = ma
    return ma
print(x(0,-1))
# print(po)


