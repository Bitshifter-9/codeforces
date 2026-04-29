s=input()
ans=[]
se=set({"a","e","i","o","u","A","E","I","O","U"})
def x(m):
    if m==len(s):
        return
    if s[m] in se:
        ans.append(1)
    x(m+1)
x(0)
print(len(ans))
