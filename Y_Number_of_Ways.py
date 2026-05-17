s,e=map(int,input().split())
ans=[]
def x(i,arr):
    if i>e:
        return
    arr.append(i)
    if i==e:
        m=arr[:]
        m.sort()
        if m not in ans:
            ans.append(m)
    x(i+1,arr)
    x(i+2,arr)
    x(i+3,arr)
    arr.pop()
x(s,[])
print(len(ans))
# ans.add([1,2])
